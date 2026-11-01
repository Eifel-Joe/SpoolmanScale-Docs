# Waveshare 7 and 7B

This fork runs on two Waveshare boards next to the WT32-SC01 Plus. The parts are the same as for the original's scale (PN532 NFC reader, NAU7802 and load cell, see the [original's parts list](https://niko11111.github.io/SpoolmanScale-Docs/build/bom/)); only the board, the wiring and the enclosure differ.

| Board | Module | Firmware environment |
|---|---|---|
| ESP32-S3-Touch-LCD-7B, 1024×600 | ESP32-S3, 16 MB flash, 8 MB PSRAM | `waveshare-s3-lcd7b` |
| ESP32-S3-Touch-LCD-7, 800×480 | ESP32-S3-WROOM-1-N16R8, 16 MB flash, 8 MB PSRAM | `waveshare-s3-lcd7` |

The 7 and the 7B are different boards with a firmware each: the I/O expander of the 7B is a CH32V003, that of the 7 a CH422G, and they are spoken to differently. Each refuses the other's image. Not supported: the ESP32-S3-LCD-7 without touch.

## Enclosure

👉 [7" Spoolman T-Scale](https://makerworld.com/en/models/3429397-7-spoolman-t-scale-waveshare-esp32-s3-touch-7) by wolfrage76 on MakerWorld, one enclosure for both boards: the 7B has the same outline as the 7.

## Wiring

The PN532 and the NAU7802 share one I2C bus, as on the WT32, on the board's **UART2 connector**.

| Signal | ESP32-S3 pin | Where on the board | Connect to |
|---|---|---|---|
| SDA | GPIO43 (TXD) | UART2 connector | PN532 SDA and NAU7802 SDA |
| SCL | GPIO44 (RXD) | UART2 connector | PN532 SCL and NAU7802 SCL |
| 3V3 | – | UART2 connector | PN532 VCC and NAU7802 VIN |
| GND | – | UART2 connector | PN532 GND and NAU7802 GND |
| RST (optional) | GPIO6 | 7: sensor connector · 7B: connector labelled GPIO | PN532 RSTPD_N |

- Set the **UART selection switch** next to the connector to **UART2**. In the UART1 position the board's USB to UART chip drives one of the two pins, and the sensors do not answer.
- The UART2 connector supplies 3.3 V; the PN532 and the NAU7802 run on it.
- Check the pin order against the labels printed on your board before connecting anything: it is not the order of the WT32 cable.
- The load cell connects to the NAU7802 as in the [original's wiring guide](https://niko11111.github.io/SpoolmanScale-Docs/build/wiring/).

!!! danger "Never connect the PN532 to the board's own I2C connector"
    That bus carries the board's I/O expander, which answers on the PN532's address (0x24). The reader would switch off the backlight and the SD card with every frame it is sent.

## Power and USB

Use the connector labelled **USB**, not the one labelled UART, for power, flashing, the serial log and the web flasher's WiFi setup.

## What is different on these boards

- **The picture** is the 480×320 interface of the WT32, enlarged until it fills the panel: about 11 % wider on the 7, about 14 % on the 7B. Every screen and every setting is otherwise the same.
- **Brightness** dims the backlight of the 7B itself (since 0.8.6-beta.16; before, the picture was dimmed). The backlight of the 7 can only be switched on and off, so on the 7 the picture is dimmed.
- **SD card:** the slot on the board takes the log, as on the WT32.
- **Updates** download the board's own image; the upload in the browser refuses an image built for another board. See [Flashing and updates](../use/updates.md).

## Building it yourself

From the repository with PlatformIO, for example `pio run -e waveshare-s3-lcd7b -t upload`. How a board is added to the firmware is described in [BUILDING.md](https://github.com/Eifel-Joe/SpoolmanScale/blob/HEAD/BUILDING.md#adding-a-board).
