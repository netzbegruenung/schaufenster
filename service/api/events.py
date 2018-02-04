# coding: utf8

import requests
import icalendar
from datetime import datetime
from datetime import date

class Client(object):

    def __init__(self, url, timezone=None):
        self.url = url
        self.timezone = timezone
        self.events = []
        self.__load()

    def __load(self):
        r = requests.get(self.url)
        r.raise_for_status()

        cal = icalendar.Calendar.from_ical(r.text)
        self.events = []

        for event in cal.walk('vevent'):
            title = None
            description = None
            if "SUMMARY" in event:
                title = event["SUMMARY"]
            if "DESCRIPTION" in event:
                description = event["DESCRIPTION"]
            dtstart = event["DTSTART"].dt
            dtend = event["DTEND"].dt
            self.events.append({
                "title": title,
                "description": description,
                "start": dtstart,
                "end": dtend,
            })

    def next_events(self, num=10):
        """
        Returns the next num events from the calendar
        """
        now = datetime.utcnow()
        out = []
        for event in self.events:
            end = event["end"]
            if isinstance(end, date):
                end = datetime.combine(end, datetime.min.time())
            if end > now:
                out.append(event)
        return out
