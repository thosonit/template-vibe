#!/usr/bin/env python3
"""Derive the five primary-family tokens of the DESIGN.md template from one brand hex.

Usage: derive_primary.py "#0F766E"

Prints YAML ready to paste into the `colors` front matter, then the contrast ratio of every
pair the template relies on. Exit code 1 if a pair is below 4.5:1 or the hue sits within 30
degrees of the error color, so the caller must adjust the brand color or the output.
"""
import colorsys
import sys

ERROR_HEX = "#CC3311"
NEUTRAL_DARK = "#262626"
AA = 4.5


def to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)


def luminance(h):
    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in to_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def hls(h):
    r, g, b = to_rgb(h)
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    return hue, light, sat


def from_hls(hue, light, sat):
    return to_hex(colorsys.hls_to_rgb(hue, max(0, min(1, light)), max(0, min(1, sat))))


def derive(brand):
    hue, light, sat = hls(brand)
    primary = brand
    # on-primary: white if it reaches AA, else the template's dark neutral; darken the brand as a last resort.
    on_primary = "#FFFFFF"
    while contrast(primary, on_primary) < AA:
        if contrast(primary, NEUTRAL_DARK) >= AA:
            on_primary = NEUTRAL_DARK
            break
        light -= 0.01
        primary = from_hls(hue, light, sat)
    _, light, sat = hls(primary)
    # hover moves away from the text color so the pair keeps its contrast.
    step = -0.07 if on_primary == "#FFFFFF" else 0.06
    hover = from_hls(hue, light + step, sat)
    if contrast(hover, on_primary) < AA:
        hover = primary
    container = from_hls(hue, 0.93, min(sat, 0.85))
    # on-primary-container: same hue, walk darker until it reads on the container.
    oc_light = min(light, 0.45)
    on_container = from_hls(hue, oc_light, sat)
    while contrast(container, on_container) < AA and oc_light > 0.05:
        oc_light -= 0.01
        on_container = from_hls(hue, oc_light, sat)
    return {
        "primary": primary,
        "on-primary": on_primary,
        "primary-container": container,
        "on-primary-container": on_container,
        "primary-hover": hover,
    }


def main():
    if len(sys.argv) != 2 or not sys.argv[1].startswith("#") or len(sys.argv[1]) != 7:
        sys.exit('usage: derive_primary.py "#RRGGBB"')
    brand = sys.argv[1].upper()
    t = derive(brand)
    for k, v in t.items():
        print(f'  {k}: "{v}"')
    pairs = [
        ("primary", "on-primary"),
        ("primary-hover", "on-primary"),
        ("primary-container", "on-primary-container"),
    ]
    bad = False
    print()
    for bg, fg in pairs:
        r = contrast(t[bg], t[fg])
        bad |= r < AA
        print(f"{fg} on {bg}: {r:.1f}:1 {'ok' if r >= AA else 'BELOW 4.5'}")
    r = contrast("#FFFFFF", t["primary"])
    print(f"primary on a white surface: {r:.1f}:1 {'ok' if r >= AA else 'BELOW 4.5 (links and focus rings)'}")
    bad |= r < AA
    dh = abs(hls(t["primary"])[0] - hls(ERROR_HEX)[0]) * 360
    dh = min(dh, 360 - dh)
    print(f"hue distance from error: {dh:.0f} degrees {'ok' if dh >= 30 else 'TOO CLOSE (< 30)'}")
    bad |= dh < 30
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
