# Spulen anlegen

Das Original legt an der Waage eine Spule aus einem Bambu-Tag oder einem leeren NTAG an und kopiert eine Spule, die auf der Waage liegt (siehe [Doku des Originals](https://niko11111.github.io/SpoolmanScale-Docs/de/use/first-spools/)). Dieser Fork fügt hinzu:

- Spulen **ohne Wiegen und ohne Aufkleber** anlegen, mehrere auf einmal, für eine Lieferung;
- **Sorte eingeben**, für ein Filament, das weder im Bestand noch in der Filament-Datenbank steht;
- mit BamBuddy und Spoolman eine **Kopie, die alle Felder** ihrer Vorlage übernimmt;
- den **Spulentyp** beim Anlegen aus einem Bambu-Tag;
- **Suchen** in den Listen und Tastaturen in der Sprache der Waage.

## Spule ohne Wiegen und ohne Aufkleber anlegen

*0.8.6 Vorabversion*

Für Rollen, die noch verschweißt sind, oder die in den Bestand sollen, bevor sie je auf der Waage liegen.

1. Ist keine Spule auf dem Schirm, heißt die rechte Taste des Hauptschirms **Spule anlegen** (mit einer Spule auf dem Schirm **Heute getrocknet**).
2. Quelle wählen: Kopie einer **Aktiven Spule** oder einer **Archivierten Spule**, Kopie über ihre Nummer (**Spoolman-ID eingeben**), **Neu aus Datenbank** oder **Sorte eingeben**.
3. Die Spule wird **nicht gewogen**, auch wenn etwas auf der Waage liegt: Sie beginnt voll, mit der Füllmenge ihrer Quelle als Nenngewicht. Hat die Quelle keine, fragt die Karte sie mit **Füllmenge** ab (100 bis 5000 g).
4. Mit BamBuddy und Spoolman kommt vorher die Liste der Spulentypen, ohne Gewicht (siehe [Wiegen und Leerspulen](weighing.md)).
5. **Anlegen**. Die Waage zeigt die neue Spule wie nach **Spule per ID**; in der Statuszeile steht „Spule <Nr.> angelegt - ohne Tag“. Bei einer Rolle von Bambu Lab steht dort stattdessen „Spule <Nr.> - Chip vor AMS auflegen“: den Chip der Rolle auf den Leser legen, bevor die Rolle in ein AMS kommt, sonst legt BamBuddy eine zweite Spule für sie an.
6. **Lagerort wählen**: dieselbe Liste wie **Mehr Info → Lagerort**, egal wie *Ortsabfrage bei Entnahme* steht. Eine Kopie hat schon den Lagerort ihrer Vorlage; die Liste kommt trotzdem. Ohne Wahl geschlossen, bleibt der Lagerort, wie er ist.
7. Ist ein Etikettendrucker eingerichtet: **Etikett drucken?** – es druckt wie **Mehr Info → Etikett drucken**, mit dem Lagerort darauf.

Ein Aufkleber wird später verknüpft, wenn die Rolle geöffnet ist: Aufkleber auf den Leser legen und **Verknüpfen** wählen, wie bei jeder Spule.

### Mehrere gleiche Spulen

Auf der Karte öffnet **Anzahl 1** oben rechts die Zahl gleicher Spulen, bis zu 10. Sie bekommen dieselbe Quelle, dasselbe Filament, denselben Spulentyp, dieselbe Füllmenge und denselben Preis und werden nacheinander angelegt. Scheitert eine, hält die Waage an, behält die angelegten und nennt sie. Danach zeigt eine Übersicht alle neuen Nummern, der Lagerort wird einmal für alle gewählt, und **<n> Etiketten drucken?** druckt je Spule ein Etikett.

### Ins AMS

**Mehr Info → Ins AMS** (BamBuddy mit AMS) öffnet die Fachwahl für jede Spule auf dem Schirm, die nicht archiviert ist, mit und ohne Aufkleber, mit und ohne Wägezelle. Das Gewicht bleibt, wie es ist.

## Sorte eingeben

*seit 0.8.5*

Für eine Spule, deren Filament weder im Bestand noch in der Filament-Datenbank steht. Wo es das gibt:

- **Neu / Kopie → Sorte eingeben**,
- auf der Karte für einen unbekannten Tag, **Nicht in Spoolman** (dort steht dein Backend) **→ Sorte eingeben**,
- in **Neu aus Datenbank** am Ende der Herstellerliste: **Nicht dabei? Sorte eingeben**,
- in **Spule anlegen** (siehe oben).

Die Schritte sind Marke, Material, Linie, Farbe, Füllmenge und Spule. In jedem Schritt wählst du zuerst aus der Filament-Datenbank und dem eigenen Bestand; **Neu anlegen** ist nur für das, was fehlt. Ein getippter Name, der einem vorhandenen nahekommt, bekommt einen Hinweis („Gibt es schon: …“), damit dasselbe Filament nicht unter zwei Schreibweisen doppelt entsteht. Farben werden auch aus den anderen Materialien der Marke angeboten.

Nach den Schritten kommt die gewohnte Anlege-Karte (Spulentyp, Preis, Aufkleber verknüpfen).

- **Dichte:** Spoolman braucht sie für jedes neue Filament. Die Waage sucht auch über den Produktnamen in der Filament-Datenbank (Bambu „Support for ABS“ → 1,16 g/cm³). Findet sie keine, heißt die linke Taste der Karte **Dichte** und öffnet ein Zahlenfeld (0,50 bis 4,00 g/cm³). *0.8.6 Vorabversion*
- **Namen hinter BamBuddy:** Ein neues Filament heißt „<Material>“ oder „<Material> <Linie>“, wie BamBuddy seine eigenen benennt; der Farbname kommt an die Spule. BamBuddy benennt ein Filament bei jeder Änderung ohnehin so um.

## Kopie mit allen Feldern

*seit 0.8.5* · BamBuddy mit Spoolman

Eine Kopie hängt am Spoolman-Filament ihrer Vorlage und übernimmt Slicer-Profil, Profile je Druckermodell, K-Profile, Preis pro kg, Lagerort und Lieferanten. Die Kopier-Karte zeigt sie, und der Preis pro kg lässt sich dort ändern. Ging etwas nicht mit, sagt die Waage, was („Kopie angelegt, ohne: …“).

Warum das zählt: BamBuddy setzt das Profil einer Spule ins AMS-Fach, und die AMS-Ersatzrolle koppelt nur Fächer mit gleichem Profil und gleicher Farbe. Eine Kopie ohne Profil würde das brechen.

## Spulentyp beim Anlegen aus einem Bambu-Tag

*0.8.6 Vorabversion* · BamBuddy, mit und ohne Spoolman

**Spule aus Tag anlegen?** fragt zuerst nach dem Spulentyp, wie Kopieren und **Neu aus Datenbank** es schon tun. Die Liste zeigt die Typen von „Bambu Lab“, der nächste an 250 g ist markiert, und **Ohne Typ**, das die Spule wie bisher anlegt. Ein Nachfüllpack auf einer anderen Spule bekommt so sein echtes Leergewicht. Die Liste kommt nur, wenn eine Spule auf der Waage liegt.

## Suche und Tastaturen

*0.8.6 Vorabversion*

- Eine **Lupe** in der Kopfzeile der Spulentyp-Liste und der Farblisten (**Sorte eingeben**, Schritt Farbe; **Neu aus Datenbank**, Farbgruppen und Einträge) öffnet die Tastatur. Nach einem Wort zeigt die Liste nur Einträge, deren Name es enthält, egal ob groß oder klein, auch mit Umlauten und Akzenten. Das Wort steht in der Kopfzeile mit einem ×, das die Suche beendet.
- Die **Tastaturen** folgen der Sprache der Waage: Deutsch QWERTZ mit ä ö ü ß, Französisch AZERTY mit é è à ç und den übrigen Akzenten auf einer eigenen Seite, Englisch wie bisher. Die Tastatur für das WLAN-Passwort behält die Anordnung der Sprache, ohne Umlaute.
