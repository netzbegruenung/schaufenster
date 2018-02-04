# Schaufenster Service

Dies ist ein Webservice zur Erzeugung dynamischer Inhalte für
Digital Signage Anwendungen.

_Anwendungsbeispiel:_

Auf einer digitalen Anzeigetafel soll stets aktuell der nächste Sitzungstermin
angezeigt werden. Hierfür geben wir eine iCal-Kalender-URL an
und bekommen dafür Titel und weitere Details der nächsten Termine in diesem
Kalender zurück.

## API

### `GET /events/` - Die nächsten Termine eines iCal Kalenders ausgeben

Request URL Parameter:

- `ical_url`: Adresse des iCal-Kalenders (erforderlich).
- `num`: Maximale Anzahl der Termine, die ausgegeben werden.
- `charset`: Zeichensatz der iCal-Quelle. Normalerweise wird der Zeichensatz
  angenommen, den der Webserver im `Content-type` header angibt. Mit diesem
  Parameter kann der Wert des Servers überschrieben werden. Beispiel: `charset=utf-8`.

Ausgabe:

```json
[
  {
    "title": "Karfreitag",
    "start": "2018-03-30",
    "end": "2018-03-31"
  },
  ...
]
```

Liste mit Terminen als JSON Array. Jeder Termin enthält:

- `title`: Titel des Termins
- `start`: Start-Datum (oder Datum/Uhrzeit) des Termins
- `end`: (optional) Enddatum (oder Datum/Uhrzeit) des Termins
