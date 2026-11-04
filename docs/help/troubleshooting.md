# Troubleshooting

For the scale itself (NFC reader, load cell, calibration, backends) the original's [troubleshooting](https://niko11111.github.io/SpoolmanScale-Docs/help/troubleshooting/) applies; the scale also explains most faults on its own screen. Here is what is specific to this fork and its boards.

## Waveshare 7 and 7B

| What you see | Why | What to do |
|---|---|---|
| Neither the NFC reader nor the NAU7802 is found | The UART selection switch is on UART1: the board's USB to UART chip then drives one of the two pins | Set the switch next to the UART2 connector to **UART2** |
| Backlight and SD card go off as soon as the reader is connected | The PN532 is on the board's own I2C connector, where the I/O expander answers on the same address | Move the PN532 to the **UART2 connector** |
| The board is not found when flashing, or there is no serial log | The cable is in the connector labelled UART | Use the connector labelled **USB** |
| The board is not found even on the USB connector | It is not in download mode | Hold **BOOT**, press and release **RESET**, release **BOOT**, try again |
| The upload in the browser refuses the file | The file is for another board, or it is a factory image | Take your board's file without `_factory`: `SpoolmanScale-waveshare-s3-lcd7b_<version>.bin` for the 7B, `…-lcd7_…` for the 7 |
| The screen stays dark with the 7's firmware on a 7B (or the other way round) | The two boards speak to their I/O expander differently | Flash the factory image of your board |
| Brightness changes the picture, not the backlight | On the 7 on purpose: its backlight can only be switched on and off. The 7B dims its backlight since 0.8.6 | On the 7B: update |

## Updates

| What you see | What to do |
|---|---|
| The scale is not offered a pre-release | Switch on **Pre-release** under **Settings → System → Firmware Update → Update via GitHub**, or set **Channel** to **Pre-release** on the web page **Firmware** |
| The scale still looks for updates at the original | Upload this fork's file once by hand, see [Flashing and updates](../use/updates.md#moving-over-from-the-original) |
| The firmware page says memory is too short for the check | Use **Check for Updates** at the scale, or upload the file; the scale's log shows the refusal |

## Klipper printers

The connection test names the step that failed and what to do, see [Klipper printers](../use/klipper.md#adding-a-printer). A spool is only assigned to a printer whose last test passed.

## Reporting a problem

Problems with the Waveshare boards or with anything this fork adds: [open an issue at the fork](https://github.com/Eifel-Joe/SpoolmanScale/issues), with the scale's log (**Logs**) and, if it helps, a screenshot. Please do not report them to the original project.
