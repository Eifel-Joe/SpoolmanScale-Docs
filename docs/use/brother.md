# Brother label printer

*since 0.8.5* · every backend

Next to the Bluetooth printers of the original (Phomemo, NIIMBOT, see the [original's documentation](https://niko11111.github.io/SpoolmanScale-Docs/use/printers/)), this fork prints on a **Brother QL-810W or QL-820NWB over WiFi**: the scale renders the label and sends it to the printer itself, no PC or app needed. Tested on a QL-820NWBc with **DK-11209** labels (62 × 29 mm). Black only.

## Setting it up

1. **On the printer**, set the command mode to **Raster** once, in the printer's own menu. New printers come set to "P-touch Template" and then print nothing.
2. **At the scale: Settings → Connection → Label printer** chooses **Off**, **Bluetooth** or **WiFi**. WiFi takes effect at once; Bluetooth restarts the scale. The settings of a Bluetooth printer stay saved.
3. **Web interface → Printer:** the printer's IP address (the printer must be on the same WiFi), the label, and the print position with a calibration page. A test print shows its verdict on the scale as well.

## Printing

As with any label printer: **More info → Print label**, after creating a spool (**Print label?**), or from the label editor in the browser (**Labels**). The card "Sent" fades after 2 s; if the printer reports a problem or the connection breaks in the 10 s after, the card comes back and says so. A label does not hold up the scale.

## Label text

*0.8.6 pre-release* · every printer the scale renders for (Brother, Bluetooth printers, the preview)

- The lines under the header take the **largest font** in which every chosen line fits the label, in width and in height, without making the QR code smaller. Fewer lines, larger text.
- **Colour as RGB** in the label editor (spool and filament labels, off by default) adds a line such as "RGB: 242, 242, 232" under the colour. Bambu Studio and OrcaSlicer take a colour as RGB, so the colour can be set there exactly as it is stored. Not for transparent, multicolour or colours without a valid hex value.
