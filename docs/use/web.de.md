# Weboberfläche

Die eigenen Webseiten der Waage funktionieren wie im Original (siehe [Doku des Originals](https://niko11111.github.io/SpoolmanScale-Docs/de/use/web/)). Dieser Fork fügt eine Einstellungs-Sicherung hinzu, eine Live-Seite für die Wägezelle, die Klipper-Seite (siehe [Klipper-Drucker](klipper.md)) und Downloads aus der in BamBuddy eingebetteten Weboberfläche.

## Am Gerät eingeschaltete Bereiche

Zwei Bereiche sind ab Werk aus, weil sie ohne Passwort etwas ändern. Eingeschaltet werden sie an der Waage unter **Einstellungen → System → Weboberfläche**:

- **Einstellungen:** Listenlimits, Trocknung, Anzeige, Zugangsdaten des Backends, die Einstellungs-Sicherung, das Zubehör an der Spule, die Seite **Waage** und die Seite **Klipper**;
- **Wartung:** Firmware-Upload, Logs, Bildschirmfotos, Neustart und Tag-Schreiben; außerdem eine Sicherung mit WLAN-Zugang und API-Schlüsseln.

## Sichern und wiederherstellen

*seit 0.8.5* · **Einstellungen → Sichern und wiederherstellen**

- **Einstellungen herunterladen** speichert alle Einstellungen der Waage als eine Datei: Kalibrierung, Backend, Anzeige, Zubehör, Drucker. Mit **Mit WLAN-Zugang und API-Schlüsseln** (braucht *Wartung*) kommen die Geheimnisse mit in die Datei; ohne bleiben sie auf der Waage.
- **Sicherung einspielen** übernimmt eine solche Datei genau: Was nicht in der Datei steht, fällt auf den Werkswert zurück. Danach startet die Waage neu.
- Fakten des Geräts selbst (Firmware-Stand, Reset-Prüfung, Protokollgrenze) und der Web-Zugang (Bereiche und PIN, an der Waage gesetzt) reisen nicht mit.

Gut vor einem Factory-Image oder um die Einstellungen auf eine andere Waage zu bringen.

## Seite Waage

*seit 0.8.5* · **Waage → Waage live**

Live von der Wägezelle: der gefundene Wandler, der Rohwert, das Gewicht, seine Streuung und der Kalibrierfaktor. Auf die Schale drücken, und der Rohwert steigt. Ein schneller Blick auf Verkabelung und Kalibrierung, ohne das Gehäuse zu öffnen.

## Downloads in BamBuddy

*0.8.6 Vorabversion*

BamBuddy kann die Weboberfläche der Waage in seiner eigenen Seite zeigen, in einem Rahmen, der keine Downloads erlaubt. Dort öffnet jeder Download (die Einstellungs-Sicherung, ein Bildschirmfoto, das Protokoll) ein kleines eigenes Fenster. Bei einer einzelnen Datei bleibt es offen, zeigt „Gespeichert: <Dateiname>“ und hat einen Knopf **Schließen**, damit der Download-Hinweis des Browsers sichtbar bleibt. Bildschirmfotos lassen sich auch alle auf einmal speichern.

## Bildschirmfotos des Displays

Wie im Original: **Logs → Display-Screenshot** nimmt ein Bild des Schirms auf, oder zwei Finger eine Sekunde aufs Display legen, bis es kurz dunkel blinkt. Bis zu 6 Bilder bleiben auf der Waage bis zum Neustart, zum Speichern, Kopieren oder Löschen. Auf einer Waveshare-Platine hat das Bild die Größe der Oberfläche, 480×320, nicht die des Panels.
