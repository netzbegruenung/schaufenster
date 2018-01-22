# Yodeck

[Yodeck](https://www.yodeck.com/) ist ein kommerzieller Anbieter für Digital
Signage Software. Die Lösung kann für einen Bildschirm kostenlos genutzt werden.

Eine Installation ist lediglich für den Client (der am Monitor angeschlossen
wird) nötig. Die Steuerung erfolgt über den Dienst von Yodeck, der über eine
zentrale Admin-Oberfläche verfügt.

## Voraussetzungen

- Raspberry Pi 2 oder neuer
- Monitor mit HD-Anschluss
- Kabel für Monitor, Stromversorgung
- Wifi oder Ethernet-Netzwerk
- SD-Karte mit mind. 8 GB
- SD-Kartenleser
- [Etcher](https://etcher.io/) oder eine andere Software zum Schreiben eines ISO-Image auf SD-Karte
- Ein kostenloser Benutzeraccount bei [app.yodeck.com](https://app.yodeck.com/)

## So geht's

### 1. Raspberry Pi Software herunter laden

Lade das [gezippte Image](http://repo.yodeck.com/files/RaspberryPi_Yodeck.zip)
herunter und entpacke die Datei.

```
wget http://repo.yodeck.com/files/RaspberryPi_Yodeck.zip
unzip RaspberryPi_Yodeck.zip
```

### 2. Schreibe das Image auf SD-Karte

Mit Etcher geht das so:

- Öffne Etcher.
- Wähle als Image-Datei die Datei aus, die du soeben durch Entpacken des
  Downloads bekommen hast.
- Stecke die SD-Karte deines Raspberry Pi in den Kartenleser.
- Etcher erkennt normalerweise automatisch, dass eine SD-Karte eingelegt wurde.
- Klicke den "Flash" Button in Etcher.
- Warte, bis Etcher fertig ist und das Ergebnis überprüft hat.
- Entferne die SD-Karte aus Deinem Kartenleser.

**Achtung:** Vorher auf der SD-Karte gespeicherte Inhalte gehen dabei verloren.

### Konfiguration

Damit der Player sich mit dem Internet verbinden kann, müssen noch ein paar
Einstellungen vorgenommen werden.

Stecke zunächst die SD-Karte, die Du soeben entfernt hast, wieder zurück in den
Kartenleser (nicht des Raspberry Pi!). Öffne dann die Datei `SETTINGS.txt` im
Wurzelverzeichnis der SD-Karte mit einem Texteditor.

#### Netzwerk

Als erstes kannst Du hier die notwendigen Netzwerkeinstellungen vornehmen. Wie
diese genau aussehen sollen, hängt von den Gegebenheiten ab. Angenommen, Du hast
ein offenes und unverschlüsseltes WLAN zur Verfügung, sieht die Konfiguration
in etwa so aus:

```
[WIFI]
ssid = NameDesWLAN
connect_to_open_networks = true
```

Hier ein Beispiel für ein mit WPA/WPA2-PSK verschlüsseltes WLAN:

```
[WIFI]
ssid = NameDesWLAN
key = MeinWLANPasswort
mode = WPA
```

Weitere Fälle können auf einer [Yodeck Support-Seite](http://support.yodeck.com/knowledgebase/articles/776754-yodeck-manual-configuration-guide) eingesehen werden.

#### Geräte-Kennung

Bei Yodeck hat jeder Player eine eindeutige ID, damit man jeden Player unabhängig
von anderen verwalten und bespielen kann.

Als erstes kannst Du unter [Monitors](https://app.yodeck.com/index.html#main/device)
im Admin-Tool, falls noch nicht geschehen, einen Monitor anlegen. Dort
wird eine `Screen ID` angezeigt. Diese trägst Du an der entsprechenden
Stelle in der Datei `SETTINGS.txt` als `deviceid` ein:

```
[REGISTRATION]
deviceid = 5f8d8e7ad1703f41a6b5c8effb612583
```

Schließlich speicherst du die Änderungen an der Datei und entfernst
die SD-Karte aus dem PC.

### Raspberry Pi hochfahren

- Lass den Raspberry Pi zunächst ohne Stromversorgung
- Schließe einen Monitor an den Raspberry Pi an
- Stecke die soeben geflashte SD-Karte in Deinen Raspberry Pi
- Stecke nun die Stromversorgung ein.

Wenn alles gut läuft, brauchst du nun am Player nichts mehr zu machen.

### Inhalte erstellen

Die Inhalte werden komplett über das Admin-Tool im Browser verwaltet.
Die Möglichkeiten sind recht umfangreich und würden den Rahmen dieser
Anleitung sprengen. Mit ein bisschen ausprobieren klappt das schon!

**Ein Hinweis:** Änderungen an den Inhalten müssen explizit auf Deinen
Player übertragen werden. Dazu erscheint im Admin-Tool, sobald es
änderungen gibt, ein roter Button, den Du anklickst, sobald Du möchtest,
dass der Player die neuen Inhalte übernimmt.

## Siehe auch

- [Creating a Yodeck Player](https://www.yodeck.com/docs/display/YO/Creating+a+Yodeck+Player)
- [Yodeck Manual Configuration Guide](http://support.yodeck.com/knowledgebase/articles/776754-yodeck-manual-configuration-guide)
