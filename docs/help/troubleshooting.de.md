# Fehlersuche

Für die Waage selbst (NFC-Leser, Wägezelle, Kalibrierung, Backends) gilt die [Fehlersuche des Originals](https://niko11111.github.io/SpoolmanScale-Docs/de/help/troubleshooting/); die meisten Fehler erklärt die Waage außerdem selbst auf dem Schirm. Hier steht, was diesen Fork und seine Platinen betrifft.

## Waveshare 7 und 7B

| Was du siehst | Warum | Was tun |
|---|---|---|
| Weder NFC-Leser noch NAU7802 werden gefunden | Der UART-Wahlschalter steht auf UART1: Dann treibt der USB-UART-Chip der Platine einen der beiden Pins | Den Schalter neben der UART2-Buchse auf **UART2** stellen |
| Hintergrundlicht und SD-Karte gehen aus, sobald der Leser angeschlossen ist | Der PN532 hängt an der eigenen I2C-Buchse der Platine, wo der IO-Baustein auf derselben Adresse antwortet | Den PN532 an die **UART2-Buchse** |
| Beim Flashen wird die Platine nicht gefunden, oder es kommt kein serielles Protokoll | Das Kabel steckt in der Buchse mit der Aufschrift UART | Die Buchse mit der Aufschrift **USB** nehmen |
| Auch an der USB-Buchse wird die Platine nicht gefunden | Sie ist nicht im Download-Modus | **BOOT** halten, **RESET** drücken und loslassen, **BOOT** loslassen, noch einmal versuchen |
| Der Upload im Browser lehnt die Datei ab | Die Datei ist für eine andere Platine oder ein Factory-Image | Die Datei der eigenen Platine ohne `_factory` nehmen: `SpoolmanScale-waveshare-s3-lcd7b_<version>.bin` für die 7B, `…-lcd7_…` für die 7 |
| Mit der Firmware der 7 bleibt eine 7B dunkel (oder umgekehrt) | Die beiden Platinen sprechen ihren IO-Baustein verschieden an | Das Factory-Image der eigenen Platine flashen |
| Die Helligkeit ändert das Bild, nicht das Hintergrundlicht | Auf der 7 gewollt: Ihr Hintergrundlicht lässt sich nur ein- und ausschalten. Die 7B dimmt ihr Hintergrundlicht seit 0.8.6 | Auf der 7B: Update |

## Updates

| Was du siehst | Was tun |
|---|---|
| Die Waage bekommt keine Vorabversion angeboten | **Vorabversionen** unter **Einstellungen → System → Firmware Update → Update via GitHub** einschalten, oder auf der Webseite **Firmware** den **Kanal** auf **Vorabversion** stellen |
| Die Waage sucht noch beim Original nach Updates | Einmal die Datei dieses Forks von Hand hochladen, siehe [Flashen und Updates](../use/updates.md#umstieg-vom-original) |
| Die Firmware-Seite meldet, der Speicher reiche für die Prüfung nicht | **Auf Updates prüfen** an der Waage nehmen oder die Datei hochladen; das Protokoll der Waage zeigt die Absage |

## Klipper-Drucker

Der Verbindungstest nennt den Schritt, der gescheitert ist, und was zu tun ist, siehe [Klipper-Drucker](../use/klipper.md#drucker-eintragen). Zugeordnet wird nur zu einem Drucker, dessen letzter Test bestanden ist.

## Ein Problem melden

Probleme mit den Waveshare-Platinen oder mit etwas, das dieser Fork dazu hat: [Issue beim Fork öffnen](https://github.com/Eifel-Joe/SpoolmanScale/issues), mit dem Protokoll der Waage (**Logs**) und, wenn es hilft, einem Bildschirmfoto. Bitte nicht beim Original melden.
