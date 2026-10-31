# SpoolmanScale Docs – Eifel-Joe fork

Documentation of the [Eifel-Joe fork](https://github.com/Eifel-Joe/SpoolmanScale) of [SpoolmanScale](https://github.com/Niko11111/SpoolmanScale), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

👉 **[eifel-joe.github.io/SpoolmanScale-Docs](https://eifel-joe.github.io/SpoolmanScale-Docs/)**

It describes only what the fork does differently: the Waveshare 7 and 7B, updates from the fork, creating spools, empty spools, the Brother printer, Klipper printers and the additions to the web interface. Everything else is in the [original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/), which these pages link to and do not copy.

## Languages

English and German side by side (`mkdocs-static-i18n`, suffix structure): `use/spools.md` next to `use/spools.de.md`. A page without a German file falls back to English. Menu labels are quoted from the firmware's `src/lang.cpp`, so what the pages say matches what the screen says.

## Screenshots

`docs/assets/images/{de,en}/` come from a Waveshare 7B on the firmware version the page describes: two fingers on the display for a second, then fetched from the scale's web interface (`/api/screenshot.bmp`) and converted to PNG. They show the 480×320 interface at its own size. IP addresses, WiFi names and device IDs do not go onto a published picture.

## Building

Every push to `main` builds the site with `mkdocs build --strict` and publishes it on GitHub Pages (`.github/workflows/pages.yml`).

## License

GPL-3.0-or-later, like the firmware. See [LICENSE](LICENSE).
