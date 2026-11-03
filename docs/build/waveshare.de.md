# Waveshare 7 und 7B

Dieser Fork läuft neben der WT32-SC01 Plus auf zwei Waveshare-Platinen. Die Teile sind dieselben wie für die Waage des Originals (NFC-Leser PN532, NAU7802 und Wägezelle, siehe [Stückliste des Originals](https://niko11111.github.io/SpoolmanScale-Docs/de/build/bom/)); anders sind nur Platine, Verkabelung und Gehäuse.

| Platine | Modul | Firmware-Umgebung |
|---|---|---|
| ESP32-S3-Touch-LCD-7B, 1024×600 | ESP32-S3, 16 MB Flash, 8 MB PSRAM | `waveshare-s3-lcd7b` |
| ESP32-S3-Touch-LCD-7, 800×480 | ESP32-S3-WROOM-1-N16R8, 16 MB Flash, 8 MB PSRAM | `waveshare-s3-lcd7` |

Die 7 und die 7B sind verschiedene Platinen mit je eigener Firmware: Der IO-Baustein der 7B ist ein CH32V003, der der 7 ein CH422G, und beide werden anders angesprochen. Jede lehnt das Image der anderen ab. Nicht unterstützt: die ESP32-S3-LCD-7 ohne Touch.

## Gehäuse

👉 [7" Spoolman T-Scale](https://makerworld.com/en/models/3429397-7-spoolman-t-scale-waveshare-esp32-s3-touch-7) von wolfrage76 auf MakerWorld, ein Gehäuse für beide Platinen: Die 7B hat denselben Umriss wie die 7.

## Verkabelung

PN532 und NAU7802 teilen sich wie bei der WT32 einen I2C-Bus, an der **UART2-Buchse** der Platine.

| Signal | ESP32-S3-Pin | Wo auf der Platine | Anschließen an |
|---|---|---|---|
| SDA | GPIO43 (TXD) | UART2-Buchse | PN532 SDA und NAU7802 SDA |
| SCL | GPIO44 (RXD) | UART2-Buchse | PN532 SCL und NAU7802 SCL |
| 3V3 | – | UART2-Buchse | PN532 VCC und NAU7802 VIN |
| GND | – | UART2-Buchse | PN532 GND und NAU7802 GND |
| RST (optional) | GPIO6 | 7: Sensor-Buchse · 7B: Buchse mit der Aufschrift GPIO | PN532 RSTPD_N |

- Den **UART-Wahlschalter** neben der Buchse auf **UART2** stellen. In der Stellung UART1 treibt der USB-UART-Chip der Platine einen der beiden Pins, und die Sensoren antworten nicht.
- Die UART2-Buchse liefert 3,3 V; PN532 und NAU7802 laufen damit.
- Vor dem Anschließen die Reihenfolge der Pins am Aufdruck der Platine prüfen: Sie ist nicht die des WT32-Kabels.
- Die Wägezelle kommt wie in der [Verkabelung des Originals](https://niko11111.github.io/SpoolmanScale-Docs/de/build/wiring/) an den NAU7802.

!!! danger "Den PN532 nie an die eigene I2C-Buchse der Platine"
    Auf diesem Bus sitzt der IO-Baustein der Platine, der auf der Adresse des PN532 antwortet (0x24). Der Leser würde mit jedem Befehl an ihn Hintergrundlicht und SD-Karte abschalten.

## Strom und USB

Für Strom, Flashen, das serielle Protokoll und die WLAN-Einrichtung über den Web-Flasher die Buchse mit der Aufschrift **USB** nehmen, nicht die mit UART.

**Mit Akku** gehört das Netzteil stattdessen an die Buchse mit der Aufschrift **UART** (siehe [Akku](#akku)): Nur dort lädt die Platine ihn.

## Akku

Die 7 und die 7B laden einen Lithium-Ionen-Akku an ihrer Akkubuchse und laufen mit ihm. Die 7B misst ihn außerdem (seit 0.8.6-beta.20): Der Hauptschirm zeigt den Ladestand in der obersten Zeile, beim Laden einen Blitz, warnt bei 20 % und bevor die Platine abschaltet, und startet ein Update im Akkubetrieb erst ab 50 %. Die 7 kann ihren Akku nicht messen; sie zeigt nichts und sperrt nichts. Die WT32-SC01 Plus hat keine Akkubuchse.

- **Eine Lithium-Ionen-Zelle, 3,7 V, höchstens 2000 mAh**, wie Waveshare empfiehlt, **mit eigener Schutzschaltung**: Der Wandler der Platine schaltet bei 2,7 V ab, trennt den Akku aber nicht.
- **Stecker vor dem Einstecken prüfen:** Auf der Platine ist Pin 1 Minus und Pin 2 Plus. Viele Akkus mit PH2.0-Stecker sind andersherum belegt.
- **Das Netzteil gehört an die Buchse mit der Aufschrift UART**, mindestens 1 A. Nur dort lädt die Platine den Akku; an der Buchse USB lädt sie nicht, und der Akku wird langsam leer.
- **Das erste Flashen und die Wiederherstellung nach einem fehlgeschlagenen Update über WLAN laufen über die Buchse USB** mit dem [Web-Flasher](https://eifel-joe.github.io/SpoolmanScale/), wie ohne Akku. Die Buchse UART führt nur Strom, solange der Umschalter auf UART2 steht.
- Die Prozente sind an einer 7B mit einem 2000-mAh-Lithium-Ionen-Akku bei voller Helligkeit gemessen: etwa 2½ Stunden mit einer Akkuladung bei dauernd eingeschaltetem Bildschirm; „Akku schwach“ kommt etwa 30 Minuten, „Akku fast leer“ etwa 15 Minuten vor dem Abschalten. Dimmt der Bildschirm, schaltet er ab und schläft die Waage, hält sie deutlich länger. Ein anderer Akku kann um etwa 10 % abweichen; mit gedimmtem Bildschirm zeigt die Anzeige eher einige Prozent zu viel, und die Laufzeit wird länger. Die Laufzeit richtet sich nach der Kapazität.
- **Beim Laden** folgen die Prozente der Ladezeit, gemessen an derselben 7B: von leer bis voll gut drei Stunden. Die letzten Prozent kann die Spannung nicht zeigen: Bis 95 % folgt die Anzeige ihr, 100 % kommen, wenn die Spannung zehn Minuten lang nicht mehr gestiegen ist. Nach einem Neustart am Netz mit vollem Akku zeigt die Anzeige zehn Minuten etwa 90 %, dann 100 % (seit 0.8.6-beta.21).
- **Ein leerer Akku** hält die 7B beim Start dunkel (seit 0.8.6-beta.21). Der Wandler der Platine schaltet bei 2,7 V ab und bei 3,0 V wieder ein; ein leerer Akku, der sich etwas erholt, schaltete die Waage deshalb immer wieder ein, und sie zog ihn wieder herunter. Jetzt misst die 7B den Akku, bevor Bildschirm und WLAN Strom ziehen, und wartet dunkel auf das Netzteil: Mit Netzteil an **UART** startet sie sofort, oder ein bis zwei Sekunden nach dem Einstecken. Ein Akku, der lange tiefentladen lag, wird zuerst mit kleinem Strom geladen; dann kann es ein paar Minuten dauern. Zieht man das Netzteil bei fast leerem Akku, kann die Waage weiter einmal neu starten; diesen Einbruch kann die Firmware nicht verhindern.

## Was auf diesen Platinen anders ist

- **Das Bild** ist die 480×320-Oberfläche der WT32, vergrößert, bis sie das Panel füllt: auf der 7 etwa 11 % breiter, auf der 7B etwa 14 %. Alle Schirme und Einstellungen sind sonst gleich.
- **Helligkeit** dimmt auf der 7B das Hintergrundlicht selbst (seit 0.8.6-beta.16; vorher wurde das Bild gedimmt). Das Hintergrundlicht der 7 lässt sich nur ein- und ausschalten, auf der 7 wird deshalb das Bild gedimmt.
- **SD-Karte:** Der Steckplatz der Platine nimmt das Protokoll auf, wie bei der WT32.
- **Updates** laden das Image der eigenen Platine; der Upload im Browser lehnt ein Image für eine andere Platine ab. Siehe [Flashen und Updates](../use/updates.md).

## Selbst bauen

Aus dem Repository mit PlatformIO, zum Beispiel `pio run -e waveshare-s3-lcd7b -t upload`. Wie eine Platine zur Firmware dazukommt, steht in [BUILDING.md](https://github.com/Eifel-Joe/SpoolmanScale/blob/HEAD/BUILDING.md#adding-a-board) (englisch).
