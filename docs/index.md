# SpoolmanScale – Eifel-Joe fork

This is the documentation of the [Eifel-Joe fork](https://github.com/Eifel-Joe/SpoolmanScale) of [SpoolmanScale](https://github.com/Niko11111/SpoolmanScale), the ESP32 filament scale with an NFC reader and a touchscreen by Niko11111.

It covers only what this fork does differently. Everything else, from the parts list and the WT32-SC01 Plus wiring to tags, backends and drying, is in the **[original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/)**, and it applies to this fork as well.

!!! note "Pre-releases"
    Features marked *0.8.6 pre-release* are in this fork's pre-releases, not yet in its latest stable release 0.8.5. To get them, switch on **Pre-release** at the scale, see [Flashing and updates](use/updates.md).

## What this fork adds

| | Page |
|---|---|
| The Waveshare ESP32-S3-Touch-LCD-7 and -7B next to the WT32-SC01 Plus | [Waveshare 7 and 7B](build/waveshare.md) |
| Updates, releases and the web flasher from this fork | [Flashing and updates](use/updates.md) |
| Create spools without weighing and without a tag, several at once; enter a new filament step by step; copy with all fields | [Creating spools](use/spools.md) |
| Parts on a spool, empty spool weights and spool types, raise the label | [Weighing and empty spools](use/weighing.md) |
| Brother QL-810W/820NWB over WiFi, larger label text, the colour as RGB | [Brother label printer](use/brother.md) |
| Klipper printers in the AMS view, choosing the printer from a list | [Klipper printers](use/klipper.md) |
| Settings backup, scale test page, downloads inside BamBuddy | [Web interface](use/web.md) |

## Which boards

| Board | Display | Status in this fork |
|---|---|---|
| Waveshare ESP32-S3-Touch-LCD-7B | 1024×600 | tested on hardware |
| Waveshare ESP32-S3-Touch-LCD-7 | 800×480 | built, not tested on hardware |
| WT32-SC01 Plus | 480×320 | built, not tested on hardware; the original's board |

All three run the same screens: the 480×320 interface of the WT32-SC01 Plus, enlarged on the Waveshare boards to fill the panel. The screenshots in this documentation are taken from a Waveshare 7B and show that interface at its own size.

## Problems and questions

Problems with the Waveshare boards or with anything this fork adds: [open an issue at the fork](https://github.com/Eifel-Joe/SpoolmanScale/issues). Please do not report them to the original project.
