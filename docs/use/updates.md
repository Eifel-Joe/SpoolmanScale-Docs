# Flashing and updates

A scale running this fork takes its releases, its updates and its web flasher from this fork, not from the original. Version numbers are the fork's own: this fork's 0.8.5 builds on the original's 0.8.3, and the original's 0.8.4 is a different firmware.

## First flash

Open this fork's **[web flasher](https://eifel-joe.github.io/SpoolmanScale/)** in Chrome or Edge, choose your board, connect it over USB (on a Waveshare board the connector labelled **USB**) and click the button. It installs the latest stable release and erases the settings.

Without the web flasher: every [release](https://github.com/Eifel-Joe/SpoolmanScale/releases) carries a factory image per board, one file with bootloader, partition table and firmware, written at offset 0:

```
esptool --chip esp32s3 write-flash 0x0 SpoolmanScale-waveshare-s3-lcd7b_<version>_factory.bin
```

If the board is not found: hold **BOOT**, press and release **RESET**, release **BOOT**, and try again. A factory image erases the settings; on a scale that already runs SpoolmanScale, update instead, or save the settings first (see [Web interface](web.md)).

## The files of a release

| File | Board | Use |
|---|---|---|
| `SpoolmanScale-waveshare-s3-lcd7b_<version>_factory.bin` | Waveshare 7B | first flash at offset 0 |
| `SpoolmanScale-waveshare-s3-lcd7b_<version>.bin` | Waveshare 7B | upload on the scale's web page |
| `SpoolmanScale-waveshare-s3-lcd7_<version>_factory.bin` | Waveshare 7 | first flash at offset 0 |
| `SpoolmanScale-waveshare-s3-lcd7_<version>.bin` | Waveshare 7 | upload on the scale's web page |
| `SpoolmanScale-wt32-sc01-plus_<version>_factory.bin` | WT32-SC01 Plus | first flash at offset 0 |
| `SpoolmanScale_<version>.bin` | WT32-SC01 Plus | upload on the scale's web page |

The files without a version in their name are what a scale downloads when it updates itself; each board takes its own and refuses another board's image.

## Updates at the scale

**Settings → System → Firmware Update → Update via GitHub**:

- **Pre-release** off: the scale is offered the latest stable release. On: the latest version of all, pre-releases included.
- **Auto check**: the scale looks for a new version once a day; the screen shows its answer.
- The button searches or installs. Every image is checked against the checksum published with the release before it is installed; the log then reads "complete … (verified)". The settings and the calibration are kept.

## Updates in the browser

The scale's web interface, page **Firmware**: **Channel** chooses **Release** or **Pre-release** (the same setting as on the device), **Check for updates** and **Install** fetch the image on the scale, not in the browser. **Upload a file** takes a firmware file you downloaded yourself; it must be the file of your board without `_factory`. The upload needs the section **Maintenance** switched on at the scale (see [Web interface](web.md#sections-switched-on-at-the-scale)).

## Moving over from the original

A scale that runs the original (or another fork) moves over once by hand: download your board's file from this fork's [releases](https://github.com/Eifel-Joe/SpoolmanScale/releases) and upload it on the scale's web page under **Firmware**. The settings are kept. From then on the updates come from this fork.
