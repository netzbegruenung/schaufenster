# Schaufenster Service

Dies ist ein Webservice zur Erzeugung dynamischer Inhalte für
Digital Signage Anwendungen.

_Anwendungsbeispiel:_

Auf einer digitalen Anzeigetafel soll stets aktuell der nächste Sitzungstermin
angezeigt werden. Hierfür geben wir eine iCal-Kalender-URL an
und bekommen dafür Titel und weitere Details der nächsten Termine in diesem
Kalender zurück.

## API

### `GET /feed/` - Beiträge eines RSS- oder Atom Feed ausgeben

Request URL Parameter:

- `url`: URL des Feed
- `num`: Anzahl der Einträge, die zurück gegeben werden sollen (default: 1)

Ausgabe:

```json
{
  "meta": {
    "title": "Die Grünen Rösrath",
    "link": "http://gruene-roesrath.de",
    "description": "",
    "published": null
  },
  "items": [
    {
      "title": "Informationsveranstaltung zur Start-/Landebahnsanierung am Flughafen",
      "summary": "Die Flughafen Köln/Bonn GmbH informiert am 1. März über die anstehende Sanierung der großen Start-...",
      "link": "http://gruene-roesrath.de/startseite/news-detailansicht/article/informationsveranstaltung_zur_start_landebahnsanierung_am_flughafen/",
      "published": "2018-02-19T20:15:00"
    }
  ]
}
```

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

Beispiele:

- [Der nächste Termin beim Grünen Ortsverband Rösrath](https://schaufenster-service.now.sh/events/?charset=utf8&num=1&ical_url=https%3A%2F%2Fgruene-roesrath.de%2Ftermine%2Fcal%2Fics%2F%3Ftype%3D150%26tx_cal_controller%255Bcalendar%255D%3D649)

- [Die nächsten 3 Feiertage in Deutschland](https://schaufenster-service.now.sh/events/?num=3&ical_url=http%3A%2F%2Fwww.webcal.fi%2Fcal.php%3Fid%3D75%26rid%3Dics%26wrn%3D0%26wp%3D12%26wf%3D55)

### Live Demo

Der Service ist erreichbar unter https://schaufenster-service.now.sh/events/


### `GET /luftdaten.info/v1/sensor/{sensor_id}/` - Aktuelle Messwerte eines luftdaten.info Sensors ausgeben

Mit dieser Methode können Feinstaub-Messwerte eines luftdaten.info Sensors
abgerufen werden.

Beispiel:

- https://schaufenster-service.now.sh/luftdateninfo/v1/sensor/6316/
