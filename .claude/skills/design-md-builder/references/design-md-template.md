---
version: alpha
name: "[Design system name]"
description: "[One-sentence description of the visual identity]"
colors:
  primary: "#D81B60"
  on-primary: "#FFFFFF"
  primary-container: "#FCE4EE"
  on-primary-container: "#C2185B"
  primary-hover: "#B8154F"
  secondary: "#5B6678"
  on-secondary: "#FFFFFF"
  secondary-container: "#E1E5EC"
  on-secondary-container: "#232A36"
  secondary-hover: "#495260"
  error: "#CC3311"
  on-error: "#FFFFFF"
  error-container: "#FFDDD0"
  on-error-container: "#7F2410"
  success: "#2E7D32"
  on-success: "#FFFFFF"
  success-container: "#DCF3DC"
  on-success-container: "#1B5E20"
  warning: "#F5A524"
  on-warning: "#262626"
  warning-container: "#FEF2DE"
  on-warning-container: "#855F2E"
  background: "#FAFAFA"
  on-background: "#262626"
  surface: "#FFFFFF"
  surface-container: "#F5F5F5"
  on-surface: "#262626"
  on-surface-variant: "#6B6B6B"
  outline: "#8E8E8E"
  outline-variant: "#EFEFEF"
  scrim: "#00000052"
typography:
  display-lg:
    fontFamily: Roboto
    fontSize: 57px
    fontWeight: 400
    lineHeight: 64px
    letterSpacing: -0.25px
  headline-lg:
    fontFamily: Roboto
    fontSize: 32px
    fontWeight: 400
    lineHeight: 40px
    letterSpacing: 0px
  headline-md:
    fontFamily: Roboto
    fontSize: 28px
    fontWeight: 400
    lineHeight: 36px
    letterSpacing: 0px
  title-lg:
    fontFamily: Roboto
    fontSize: 22px
    fontWeight: 400
    lineHeight: 28px
    letterSpacing: 0px
  title-md:
    fontFamily: Roboto
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0.15px
  body-lg:
    fontFamily: Roboto
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0.5px
  body-md:
    fontFamily: Roboto
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0.25px
  body-sm:
    fontFamily: Roboto
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0.4px
  label-lg:
    fontFamily: Roboto
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0.1px
  label-md:
    fontFamily: Roboto
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.5px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  control-sm: 32px
  control-md: 40px
  control-lg: 48px
  icon-sm: 20px
  icon-md: 24px
  gutter: 16px
  margin: 16px
  columns: 4
  medium:
    gutter: 24px
    margin: 24px
    columns: 8
  expanded:
    gutter: 24px
    margin: 24px
    columns: 12
rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 28px
  full: 9999px
motion:
  state-change:
    duration: 100ms
    delay: 0ms
    timingFunction: ease-out
  surface-enter:
    duration: 250ms
    delay: 0ms
    timingFunction: cubic-bezier(0.2, 0, 0, 1)
  surface-exit:
    duration: 150ms
    delay: 0ms
    timingFunction: cubic-bezier(0.3, 0, 0.8, 0.15)
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.full}"
    padding: "{spacing.lg}"
    height: "{spacing.control-md}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-primary-pressed:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-primary-loading:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.outline-variant}"
    textColor: "{colors.on-surface-variant}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.full}"
    padding: "{spacing.lg}"
    height: "{spacing.control-md}"
  button-secondary-hover:
    backgroundColor: "{colors.secondary-hover}"
    textColor: "{colors.on-secondary}"
  button-secondary-pressed:
    backgroundColor: "{colors.secondary-hover}"
    textColor: "{colors.on-secondary}"
  button-secondary-loading:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
  button-secondary-disabled:
    backgroundColor: "{colors.outline-variant}"
    textColor: "{colors.on-surface-variant}"
  button-icon:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    rounded: "{rounded.full}"
    size: "{spacing.control-md}"
  input-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-md}"
  input-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-md}"
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-md}"
  input-error:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-md}"
  helper-text:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.body-sm}"
  error-text:
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
  input-disabled:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-md}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  list-item:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
    height: "{spacing.control-lg}"
  chip:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-sm}"
  chip-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    height: "{spacing.control-sm}"
  checkbox:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    size: "{spacing.icon-sm}"
  checkbox-unchecked:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.xs}"
    size: "{spacing.icon-sm}"
  radio:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    size: "{spacing.icon-sm}"
  radio-unselected:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.full}"
    size: "{spacing.icon-sm}"
  dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.lg}"
  dialog-scrim:
    backgroundColor: "{colors.scrim}"
  alert-success:
    backgroundColor: "{colors.success-container}"
    textColor: "{colors.on-success-container}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  alert-warning:
    backgroundColor: "{colors.warning-container}"
    textColor: "{colors.on-warning-container}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  alert-error:
    backgroundColor: "{colors.error-container}"
    textColor: "{colors.on-error-container}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  progress-track:
    backgroundColor: "{colors.secondary-container}"
    rounded: "{rounded.full}"
    height: "{spacing.xs}"
  progress-indicator:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: "{spacing.xs}"
  spinner:
    textColor: "{colors.primary}"
    size: "{spacing.icon-md}"
  divider:
    backgroundColor: "{colors.outline-variant}"
    height: 1px
  link:
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  link-hover:
    textColor: "{colors.primary-hover}"
  breadcrumb-item:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.body-md}"
    height: "{spacing.control-md}"
  breadcrumb-item-current:
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    height: "{spacing.control-md}"
  pagination-item:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.full}"
    size: "{spacing.control-md}"
  pagination-item-current:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.full}"
    size: "{spacing.control-md}"
---

# [Design system name]

## Overview

[Holistic description of the look and feel: brand personality, target audience, and the emotional response the UI should evoke (playful or professional, dense or spacious). Guides high-level decisions when no explicit rule or token exists.]

## Colors

Color tokens are named by role. Each `on-*` token is the text and icon color placed on its matching background.

- **Primary (#D81B60):** Brand color. Primary buttons, links, focus.
- **On-primary (#FFFFFF):** Text and icons placed on primary.
- **Primary-container (#FCE4EE):** Tonal fill for chips and the current item in navigation.
- **On-primary-container (#C2185B):** Text and icons on primary-container.
- **Primary-hover (#B8154F):** Hover and pressed fill for primary buttons. Not a Material Design 3 role, which uses state layers; it is kept as a token because a white state layer would drop the pressed state below 4.5:1.
- **Secondary (#5B6678):** Supporting brand color for less prominent actions and accents.
- **On-secondary (#FFFFFF):** Text and icons on secondary.
- **Secondary-container (#E1E5EC):** Tonal fill for secondary elements.
- **On-secondary-container (#232A36):** Text and icons on secondary-container.
- **Secondary-hover (#495260):** Hover and pressed fill for secondary buttons.
- **Error (#CC3311):** Error states and destructive actions.
- **On-error (#FFFFFF):** Text and icons on error.
- **Error-container (#FFDDD0):** Background for error alerts.
- **On-error-container (#7F2410):** Text and icons on error-container.
- **Success (#2E7D32):** Functional color. Confirmation and completed states.
- **On-success (#FFFFFF):** Text and icons on success.
- **Success-container (#DCF3DC):** Background for success alerts and badges.
- **On-success-container (#1B5E20):** Text and icons on success-container.
- **Warning (#F5A524):** Functional color. Caution and pending states.
- **On-warning (#262626):** Text and icons on warning.
- **Warning-container (#FEF2DE):** Background for warning alerts and badges.
- **On-warning-container (#855F2E):** Text and icons on warning-container.
- **Background (#FAFAFA):** Page background.
- **On-background (#262626):** Text and icons on background.
- **Surface (#FFFFFF):** Cards, panels, inputs.
- **Surface-container (#F5F5F5):** Nested panels, sidebars, striped rows.
- **On-surface (#262626):** Main text color.
- **On-surface-variant (#6B6B6B):** Secondary text, placeholders, captions.
- **Outline (#8E8E8E):** Input borders and card outlines.
- **Outline-variant (#EFEFEF):** Dividers and subtle edges.
- **Scrim (#00000052):** Translucent layer behind dialogs and bottom sheets.

## Typography

Roboto throughout, in weights 400 (regular) and 500 (medium). Styles are grouped as display, headline, title, body and label, each in lg, md or sm. Below 600px, `display-lg` scales down to 40px with a 48px line height.

- **Display (display-lg):** Roboto 400, 57px. Hero numbers and landing headlines only.
- **Headlines (headline-lg, headline-md):** Roboto 400, 32px and 28px. Page and section titles.
- **Titles (title-lg, title-md):** Roboto 400 at 22px, 500 at 16px. Card, dialog and list headings.
- **Body (body-lg, body-md, body-sm):** Roboto 400, 16px, 14px and 12px. Reading text, with body-md as the default and body-sm for captions.
- **Labels (label-lg, label-md):** Roboto 500, 14px and 12px. Buttons, tabs, chips and form labels.

## Layout

Layout and spacing use a 4px base grid that adapts to the window size. Compact (phones) is the default; `medium` (tablets) and `expanded` (desktop) override gutter, margin and columns.

- **Xs (4px):** Tight gaps between an icon and its label.
- **Sm (8px):** Gaps between related elements inside a component.
- **Md (16px):** Default padding and the gap between components.
- **Lg (24px):** Horizontal padding of buttons and spacing between groups.
- **Xl (32px):** Spacing between sections of a screen.
- **2xl (48px):** Large separation between major blocks.
- **3xl (64px):** Page-level top and bottom spacing.
- **Control-sm (32px):** Height of chips.
- **Control-md (40px):** Height of buttons, inputs, breadcrumb links and pagination items. Every control that shares a row uses this height, and it is the base for the other sizes.
- **Control-lg (48px):** Height of list items.
- **Icon-sm (20px):** Icons inside a button with a label, and checkboxes and radio buttons.
- **Icon-md (24px):** Icons on their own and inside an icon button.
- **Fixed-height components:** When a component has a fixed height, its padding is the horizontal inset and the content is centered vertically.
- **Gutter and margin (16px):** Space between columns and around the content on compact windows.
- **Columns (4):** 4 on compact, 8 on medium and 12 on expanded windows.
- **Touch target:** Every interactive element has a hit area of at least `control-md` (40px) by 40px, even when its visible control is smaller, such as a checkbox or radio button.

## Elevation & Depth

Depth comes mainly from tonal layers: each step up the surface scale (`background`, `surface`, `surface-container`) reads as closer to the user. Shadows are reserved for elements that float above the page.

- **Level 0, flat:** `background`, no shadow. Used for the page.
- **Level 1, surface:** `surface` on `background`, with `outline-variant` where an edge is needed. Used for cards, inputs and panels.
- **Level 2, raised:** `surface-container` with shadow `0 2px 6px rgb(0 0 0 / .15)`. Used for menus and popovers.
- **Level 3, overlay:** `surface` with shadow `0 8px 24px rgb(0 0 0 / .2)`, over a `scrim` layer. Used for dialogs and bottom sheets.
- **Stack order:** page 0, sticky header 10, menus and popovers 20, dialogs and bottom sheets 50, toasts 60.
- **Dark theme:** If the system has a dark theme, shadows lose contrast on dark surfaces, so the tonal step carries the edge and level 2 and 3 shadows can be reduced.

## Shapes

Corner radii scale with the surface: the larger the surface, the larger the radius, and interactive controls are fully rounded.

- **None (0px):** Edge-to-edge images and dividers.
- **Xs (4px):** Checkboxes.
- **Sm (8px):** Chips and inputs.
- **Md (12px):** Cards and alerts.
- **Lg (16px):** Large cards and panels.
- **Xl (28px):** Dialogs and bottom sheets.
- **Full (9999px):** Buttons, badges and avatars.

## Motion & Micro-interaction

Motion is quick and understated: it confirms an action or shows where something came from, and never decorates.

- **What moves:** State changes on interactive elements (`state-change`) and surfaces entering (`surface-enter`) or leaving (`surface-exit`). A pressed button also scales to 0.97. Nothing loops except spinners, and static content does not move.
- **Duration rhythm:** Small, local changes take 100ms, leaving surfaces 150ms and entering surfaces 250ms, so larger changes take longer.
- **Easing intent:** Entering elements decelerate, leaving elements accelerate, and elements that stay on screen use a symmetric curve.
- **Restraint:** Honor `prefers-reduced-motion`, and animate `transform` and `opacity` rather than properties that force layout.

## Voice & Content Strategy

- **Tone of voice:** Clear, calm and direct. It does not use slang, exclamation marks or marketing language.
- **Capitalization:** Sentence case everywhere, including buttons, headings and menu items.
- **Terminology:** Use one term per concept across the product, and avoid synonyms for it.
- **Button and action labels:** Start with a verb and name the result, such as "Save changes", and keep the same name through the whole flow.
- **Empty, loading, and error states:** Say what happened and the next action to take. Errors never apologize and are never vague.
- **Numbers, dates, and units:** Use one format for dates, times and units across the product, with a space between a number and its unit.

## Components

Components are built only from the tokens above: color pairs from the Colors section, `rounded` and `spacing` steps, and the Typography styles. Primary and secondary buttons have hover, pressed, loading and disabled variants; chips also have a selected state; other components have a default state.

- **Buttons** — `button-primary`, `button-primary-hover`, `button-primary-pressed`, `button-primary-loading`, `button-primary-disabled`, `button-secondary`, `button-secondary-hover`, `button-secondary-pressed`, `button-secondary-loading`, `button-secondary-disabled`, `button-icon`
- **Input Fields** — `input-default`, `input-hover`, `input-focus`, `input-error`, `input-disabled`, `helper-text`, `error-text`. The schema has no border property, so edges are set here. Default: 1px `outline` border. Hover: border becomes `on-surface`. Focus: border becomes `primary` plus a 1px `primary` ring, 2px in total. Error: border and label become `error`, the value text stays `on-surface`, and the message is `error-text` with an error icon before it. Disabled: dashed `outline` border and the whole field at 60% opacity so it cannot be mistaken for a placeholder. The label is `body-sm` in `on-surface-variant` with 4px to the field; `helper-text` sits 4px below it.
- **Cards** — `card`
- **Lists** — `list-item`
- **Chips** — `chip`, `chip-selected`
- **Checkboxes and Radio Buttons** — `checkbox`, `checkbox-unchecked`, `radio`, `radio-unselected`
- **Dialogs** — `dialog`, `dialog-scrim`
- **Alerts** — `alert-success`, `alert-warning`, `alert-error`
- **Progress** — `progress-track`, `progress-indicator`, `spinner`. Use a bar when the amount done is known and a spinner when it is not, and always name what is loading.
- **Dividers** — `divider`. Use spacing first and add a divider only when groups still read as one.
- **Links** — `link`, `link-hover`. Always underlined in running text.
- **Breadcrumbs** — `breadcrumb-item`, `breadcrumb-item-current`. The last item is the current page and is not a link.
- **Pagination** — `pagination-item`, `pagination-item-current`. Shows the current page, its neighbours and the first and last page; previous and next use `button-icon`.
- **Icons:** Lucide icons at 24px, inside a `button-icon` or beside a label, and never mixed with icons from other sets.

## Do's and Don'ts

- Do name color tokens by role following Material Design 3 (`primary`, `on-primary`, `surface`, `outline`), never by hue or value.
- Do use icons from a single icon set only, which is Lucide in this system, and never mix in icons from other sets.
- Do name any additional brand color following Material Design 3 (such as `tertiary`) and define its full set of four tokens: the color, `on-` color, `-container` and `on-…-container`.
- Don't use raw hex values or fixed sizes in components where a token exists; always reference the token.
- Don't pick a primary hue within about 30° of the error hue, so brand and error surfaces stay distinguishable.
