#!/usr/bin/env python3
"""Sync the token-driven parts of design.html from DESIGN.md, then report what still needs hands.

Usage:
    sync_tokens.py DESIGN.md design.html           # rewrite design.html in place
    sync_tokens.py DESIGN.md design.html --check   # report only, write nothing

Rewrites: the `:root` custom properties (colors, spacing, controls, radii, motion, font), the
medium/expanded window overrides, the Google Fonts link, <title>, the brand name, the h1, and the
two ledes in the hero (description and the first Overview paragraph).

Reports (never edits): tokens with no matching CSS variable, color tokens missing from the
`groups` array, `pairs` below 4.5:1, and template placeholders still left in the page.
Needs PyYAML. Exit code 1 if anything was reported.
"""
import html
import re
import sys
from pathlib import Path

import yaml

AA = 4.5
PLACEHOLDER = re.compile(r"\[[A-Z][^\]\n]{8,}\]")


def read_design(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not match:
        sys.exit(f"{path}: no YAML front matter")
    return yaml.safe_load(match.group(1)), match.group(2)


def css_vars(tokens: dict) -> dict[str, str]:
    """Map DESIGN.md front matter to the template's CSS custom properties."""
    out: dict[str, str] = {}
    for key, value in tokens.get("colors", {}).items():
        out[f"--{key}"] = str(value)
    spacing = tokens.get("spacing", {})
    for key, value in spacing.items():
        if isinstance(value, dict):
            continue
        if key.startswith(("control-", "icon-")) or key in ("gutter", "margin", "columns"):
            out[f"--{key}"] = str(value)
        else:
            out[f"--space-{key}"] = str(value)
    for key, value in tokens.get("rounded", {}).items():
        out[f"--r-{key}"] = str(value)
    for name, spec in tokens.get("motion", {}).items():
        out[f"--dur-{name}"] = str(spec["duration"])
        out[f"--ease-{name}"] = str(spec["timingFunction"])
    family = first_font(tokens)
    if family:
        out["--font"] = f"{family}, system-ui, sans-serif"
    return out


def first_font(tokens: dict) -> str | None:
    for spec in tokens.get("typography", {}).values():
        return str(spec["fontFamily"])
    return None


def font_weights(tokens: dict) -> list[int]:
    return sorted({int(s["fontWeight"]) for s in tokens.get("typography", {}).values()})


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")[:6]
    chans = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in chans]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def set_vars(root_block: str, wanted: dict[str, str]) -> tuple[str, list[str]]:
    """Replace values of existing custom properties; return the new block and the vars not found."""
    missing = []
    for name, value in wanted.items():
        pattern = re.compile(rf"({re.escape(name)}\s*:\s*)([^;]+)(;)")
        if pattern.search(root_block):
            root_block = pattern.sub(lambda m: f"{m.group(1)}{value}{m.group(3)}", root_block, count=1)
        else:
            missing.append(name)
    return root_block, missing


def sync(tokens: dict, body: str, page: str) -> tuple[str, list[str]]:
    reports: list[str] = []
    root = re.search(r":root \{.*?\n\}", page, re.S)
    if not root:
        sys.exit("design.html: no :root block")
    new_root, missing = set_vars(root.group(0), css_vars(tokens))
    page = page.replace(root.group(0), new_root, 1)
    reports += [f"no CSS variable {m} in the page: add it by hand" for m in missing]

    spacing = tokens.get("spacing", {})
    for query, label in (("min-width:600px", "medium"), ("min-width:840px", "expanded")):
        spec = spacing.get(label)
        line = re.search(rf"@media \({query}\) \{{ :root \{{[^}}]*\}} \}}", page)
        if not spec or not line:
            continue
        new_line, _ = set_vars(line.group(0), {f"--{k}": str(v) for k, v in spec.items()})
        page = page.replace(line.group(0), new_line, 1)

    family, weights = first_font(tokens), font_weights(tokens)
    if family:
        wght = ";".join(str(w) for w in weights)
        link = f"family={family.replace(' ', '+')}:wght@{wght}"
        page = re.sub(r"family=[^&\"]+(?=&display=swap)", link, page, count=1)

    name, desc = str(tokens.get("name", "")), str(tokens.get("description", ""))
    overview = re.search(r"## Overview\n+(.*?)(?:\n\n|\n## )", body, re.S)
    swaps = [
        (r"(<title>)[^<]*(</title>)", name),
        (r'(<span class="brand">)[^<]*(</span>)', name),
        (r'(<h1 id="h-overview"[^>]*>)[^<]*(</h1>)', name),
        (r'(<h1 id="h-overview"[^>]*>[^<]*</h1>\s*<p class="lede">)[^<]*(</p>)', desc),
    ]
    if family:
        swaps.append((r"(<dt>)[^<]*(</dt><dd>The only typeface)", family))
    if overview:
        paragraph = " ".join(overview.group(1).split())
        swaps.append(
            (r'(<h1 id="h-overview"[^>]*>[^<]*</h1>\s*<p class="lede">[^<]*</p>\s*<p class="lede">)[^<]*(</p>)', paragraph)
        )
    for pattern, text in swaps:
        page = re.sub(pattern, lambda m, t=text: f"{m.group(1)}{html.escape(t, quote=False)}{m.group(2)}", page, count=1)
    return page, reports


def audit(tokens: dict, page: str) -> list[str]:
    reports: list[str] = []
    colors = {k: str(v) for k, v in tokens.get("colors", {}).items()}
    groups = re.search(r"const groups = \[(.*?)\n  \];", page, re.S)
    if groups:
        listed = set(re.findall(r"'([a-z0-9-]+)'", groups.group(1)))
        reports += [f"color token '{k}' is not in the groups array" for k in colors if k not in listed]
        reports += [f"groups lists '{k}' which DESIGN.md does not define" for k in listed - set(colors) if k[0].islower() and "-" in k]
    pairs = re.search(r"const pairs = \[(.*?)\n  \];", page, re.S)
    if pairs:
        for bg, fg in re.findall(r"\['([a-z0-9-]+)', '([a-z0-9-]+)'\]", pairs.group(1)):
            if bg not in colors or fg not in colors:
                reports.append(f"pair {fg} on {bg} uses an undefined token")
                continue
            ratio = contrast(colors[bg], colors[fg])
            if ratio < AA:
                reports.append(f"pair {fg} on {bg} is {ratio:.1f}:1, below 4.5")
    reports += [f"placeholder left in the page: {m}" for m in sorted(set(PLACEHOLDER.findall(page.split('<script>')[0])))]
    return reports


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    check_only = "--check" in sys.argv
    design_path, page_path = Path(args[0]), Path(args[1])
    tokens, body = read_design(design_path)
    page = page_path.read_text(encoding="utf-8")
    new_page, reports = sync(tokens, body, page)
    reports += audit(tokens, new_page)
    if check_only:
        verb = "would change" if new_page != page else "already in sync"
        print(f"{page_path}: {verb}")
    else:
        page_path.write_text(new_page, encoding="utf-8")
        print(f"{page_path}: written")
    for line in reports:
        print(f"  - {line}")
    sys.exit(1 if reports else 0)


if __name__ == "__main__":
    main()
