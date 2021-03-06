# -*- coding: utf-8 -*-

import requests
import icalendar
from datetime import datetime
from datetime import date
from datetime import timedelta


class Client(object):

    def __init__(self, url, charset=None):
        self.url = url
        self.charset = charset
        self.events = []
        self.timeout = 60
        self.__load()

    def __load(self):
        r = requests.get(self.url, timeout=self.timeout)
        r.raise_for_status()

        # requests normally uses encoding returned by "Content-type" header.
        # If charset is set, this overwrites the detected character encoding.
        if self.charset is not None:
            r.encoding = self.charset

        cal = icalendar.Calendar.from_ical(r.text)
        self.events = []

        for event in cal.walk('vevent'):
            title = None
            if "SUMMARY" in event:
                title = event["SUMMARY"]
            dtstart = event["DTSTART"].dt
            dtend = event["DTEND"].dt
            self.events.append({
                "title": title,
                "start": dtstart,
                "end": dtend,
            })

        # sort events by start datetime
        def getdatetime(event):
            if isinstance(event["start"], date):
                return datetime.combine(event["start"], datetime.min.time())
            return event["start"]
        self.events = sorted(self.events, key=getdatetime)

    def next_events(self, num=10):
        """
        Returns the next num events from the calendar
        """
        now = datetime.utcnow() + timedelta(hours=5)
        out = []
        for event in self.events:
            end = event["end"]
            if isinstance(end, date):
                end = datetime.combine(end, datetime.min.time())
            if end > now:
                out.append(event)
            if len(out) >= num:
                break
        return out
