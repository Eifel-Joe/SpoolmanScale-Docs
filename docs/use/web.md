# Web interface

The scale's own web pages work as in the original (see the [original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/use/web/)). This fork adds a settings backup, a live page for the load cell, the Klipper page (see [Klipper printers](klipper.md)), and downloads from the web interface embedded in BamBuddy.

## Sections switched on at the scale

Two sections are off by default, because they change things without a password. They are switched on at the scale under **Settings → System → Web interface**:

- **Settings:** list limits, drying, display, backend credentials, the settings backup, the parts on the spool, the **Scale** page and the **Klipper** page;
- **Maintenance:** firmware upload, logs, screenshots, restart and writing tags; also a backup with WiFi login and API keys.

## Backup and restore

*since 0.8.5* · **Settings → Backup and restore**

- **Download settings** saves every setting of the scale as one file: calibration, backend, display, parts, printers. With **Include Wi-Fi login and API keys** (needs *Maintenance*) the secrets go into the file as well; without it they stay on the scale.
- **Load a backup** takes such a file back exactly: what is not in the file falls back to the factory value. The scale then restarts.
- Facts of the device itself (firmware version, reset check, log limit) and the web access (sections and PIN set at the scale) do not travel with the file.

Use it before a factory image or to move the settings to another scale.

## Scale page

*since 0.8.5* · **Scale → Scale live**

Live from the load cell: the amplifier found, the raw value, the weight, its noise and the calibration factor. Press on the platform and the raw value rises. A quick check of the wiring and the calibration, without opening the case.

## Downloads inside BamBuddy

*0.8.6 pre-release*

BamBuddy can show the scale's web interface inside its own page, in a frame that does not allow downloads. There, every download (the settings backup, a screenshot, the log) opens a small window of its own. With a single file it stays open, reads "Saved: <file name>" and has a **Close** button, so the browser's download notice stays visible. Screenshots can also be saved all at once.

## Screenshots of the display

As in the original: **Logs → Display screenshot** takes a picture of the screen, or rest two fingers on the display for a second until it blinks dark. Up to 6 pictures stay on the scale until it restarts, ready to save, copy or delete. On a Waveshare board the picture has the size of the interface, 480×320, not of the panel.
