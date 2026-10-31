# SpoolmanScale Docs – Eifel-Joe fork

Documentation of the [Eifel-Joe fork](https://github.com/Eifel-Joe/SpoolmanScale) of [SpoolmanScale](https://github.com/Niko11111/SpoolmanScale), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

👉 **[eifel-joe.github.io/SpoolmanScale-Docs](https://eifel-joe.github.io/SpoolmanScale-Docs/)**

It describes only what the fork does differently: the Waveshare 7 and 7B, updates from the fork, creating spools, empty spools, the Brother printer, Klipper printers and the additions to the web interface. Everything else is in the [original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/), which these pages link to and do not copy.

## Languages

English and German side by side (`mkdocs-static-i18n`, suffix structure): `use/spools.md` next to `use/spools.de.md`. A page without a German file falls back to English. Menu labels are quoted from the firmware's `src/lang.cpp`, so what the pages say matches what the screen says.

## Screenshots

`docs/assets/images/{de,en}/` come from a Waveshare 7B and show the 480×320 interface at its own size. IP addresses, WiFi names and device IDs do not go onto a published picture (blurred where a screen shows one).

They are taken with the **documentation build** of the firmware, branch `feat/doku-bilder` of the firmware repository, which is never released and never merged: it adds `POST /api/touch` (tap, long press, swipe in 480×320 coordinates) and `POST /api/sim/weight?g=` (a simulated weight on the pad), writes nothing to any server, and names itself `v0.8.6-beta.12-doku` everywhere but on the screens that go into the pictures. For new pictures: merge the current `dev` into that branch, let the CI build it, upload the image on the scale, tap through with `/api/touch`, take each picture with `POST /api/screenshot`, fetch them with `tools/fetch_screenshots.py`, then put the released firmware back on the scale. Take a screenshot after every change of screen before tapping again: a cancel does not always lead back to the screen one expects.

## Building

Every push to `main` builds the site with `mkdocs build --strict` and publishes it on GitHub Pages (`.github/workflows/pages.yml`).

## License

GPL-3.0-or-later, like the firmware. See [LICENSE](LICENSE).
