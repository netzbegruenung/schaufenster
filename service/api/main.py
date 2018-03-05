# -*- coding: utf-8 -*-

from . import events
from . import jsonhandler
from . import feeds
from datetime import datetime
from falcon import media
from falcon_cors import CORS
import falcon
import logging
import requests


class EventsResource(object):

    def __init__(self):
        self.logger = logging.getLogger('api.' + __name__)

    def on_get(self, req, resp):
        """
        Loads an ical Calendar and returns the next events
        """
        ical_url = req.get_param("ical_url", required=True)
        charset = req.get_param("charset")
        num = int(req.get_param("num", required=False, default="10"))

        client = events.Client(url=ical_url, charset=charset)
        next_events = client.next_events(num)
        del client

        resp.media = next_events
        maxage = 60 * 60  # 1 hour
        resp.cache_control = ["max_age=%d" % maxage]

class FeedResource(object):

    def on_get(self, req, resp):
        feed_url = req.get_param("url", required=True)
        num = int(req.get_param("num", required=False, default="1"))
        c = feeds.Client(feed_url)
        resp.media = {
            "meta": c.metadata(),
            "items": c.recent_items(num=num)
        }

class ParticleSensorResource(object):

    def on_get(self, req, resp, sensor_id):
        """
        Delivers data for a particular luftdaten.info sensor
        """
        url = "http://api.luftdaten.info/v1/sensor/%s/" % sensor_id
        r = requests.get(url)

        if r.status_code == 200:
            maxage = 60 * 5  # 5 minutes
            resp.cache_control = ["max_age=%d" % maxage]
            resp.media = r.json()
        else:
            resp.media = r.text
            resp.status = str(r.status_code) + " Unknown Error"

handlers = media.Handlers({
    'application/json': jsonhandler.JSONHandler(),
})

cors = CORS(allow_all_origins=True,
            allow_all_headers=True)

app = falcon.API(middleware=[cors.middleware])

app.req_options.media_handlers = handlers
app.resp_options.media_handlers = handlers

app.add_route('/events/', EventsResource())
app.add_route('/feed/', FeedResource())
app.add_route('/luftdaten.info/v1/sensor/{sensor_id}/', ParticleSensorResource())
