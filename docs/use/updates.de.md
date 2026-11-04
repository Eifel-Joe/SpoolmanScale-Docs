# Flashen und Updates

Eine Waage mit diesem Fork bekommt Releases, Updates und Web-Flasher aus diesem Fork, nicht vom Original. Die Versionsnummern sind die des Forks: Seine 0.8.5 und 0.8.6 bauen auf der 0.8.3 des Originals auf, und die 0.8.4 des Originals ist eine andere Firmware.

## Erstes Flashen

Den **[Web-Flasher](https://eifel-joe.github.io/SpoolmanScale/)** dieses Forks in Chrome oder Edge öffnen, Platine wählen, per USB verbinden (bei einer Waveshare-Platine die Buchse mit der Aufschrift **USB**) und den Knopf drücken. Er installiert das neueste stabile Release und löscht die Einstellungen.

Ohne Web-Flasher: Jedes [Release](https://github.com/Eifel-Joe/SpoolmanScale/releases) enthält je Platine ein Factory-Image, eine Datei mit Bootloader, Partitionstabelle und Firmware, geschrieben an Adresse 0:

```
esptool --chip esp32s3 write-flash 0x0 SpoolmanScale-waveshare-s3-lcd7b_<version>_factory.bin
```

Wird die Platine nicht gefunden: **BOOT** halten, **RESET** drücken und loslassen, **BOOT** loslassen und noch einmal versuchen. Ein Factory-Image löscht die Einstellungen; auf einer Waage, die schon SpoolmanScale hat, lieber aktualisieren oder vorher die Einstellungen sichern (siehe [Weboberfläche](web.md)).

## Die Dateien eines Releases

| Datei | Platine | Zweck |
|---|---|---|
| `SpoolmanScale-waveshare-s3-lcd7b_<version>_factory.bin` | Waveshare 7B | erstes Flashen an Adresse 0 |
| `SpoolmanScale-waveshare-s3-lcd7b_<version>.bin` | Waveshare 7B | Upload auf der Webseite der Waage |
| `SpoolmanScale-waveshare-s3-lcd7_<version>_factory.bin` | Waveshare 7 | erstes Flashen an Adresse 0 |
| `SpoolmanScale-waveshare-s3-lcd7_<version>.bin` | Waveshare 7 | Upload auf der Webseite der Waage |
| `SpoolmanScale-wt32-sc01-plus_<version>_factory.bin` | WT32-SC01 Plus | erstes Flashen an Adresse 0 |
| `SpoolmanScale_<version>.bin` | WT32-SC01 Plus | Upload auf der Webseite der Waage |

Die Dateien ohne Version im Namen lädt eine Waage, wenn sie sich selbst aktualisiert; jede Platine nimmt ihre eigene und lehnt das Image einer anderen ab.

## Updates an der Waage

**Einstellungen → System → Firmware Update → Update via GitHub**:

- **Vorabversionen** aus: Die Waage bekommt das neueste stabile Release angeboten. An: die neueste Version überhaupt, Vorabversionen eingeschlossen.
- **Automatisch suchen**: Die Waage sucht einmal am Tag nach einer neuen Version; der Schirm zeigt ihre Antwort.
- Der Knopf sucht oder installiert. Jedes Image wird vor dem Installieren gegen die Prüfsumme geprüft, die mit dem Release veröffentlicht ist; im Protokoll steht dann „complete … (verified)“. Einstellungen und Kalibrierung bleiben.

## Updates im Browser

Weboberfläche der Waage, Seite **Firmware**: **Kanal** wählt **Release** oder **Vorabversion** (dieselbe Einstellung wie am Gerät), **Nach Updates suchen** und **Installieren** holen das Image auf der Waage, nicht im Browser. **Datei hochladen** nimmt eine selbst heruntergeladene Firmware-Datei; es muss die Datei der eigenen Platine ohne `_factory` sein. Der Upload braucht an der Waage eingeschaltete **Wartung** (siehe [Weboberfläche](web.md#am-gerat-eingeschaltete-bereiche)).

## Umstieg vom Original

Eine Waage mit dem Original (oder einem anderen Fork) wechselt einmal von Hand: die Datei der eigenen Platine aus den [Releases](https://github.com/Eifel-Joe/SpoolmanScale/releases) dieses Forks laden und auf der Webseite der Waage unter **Firmware** hochladen. Die Einstellungen bleiben. Danach kommen die Updates aus diesem Fork.
