# -*- coding: utf-8 -*-

import falcon
from falcon import media
import logging
from . import events
from . import jsonhandler


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
        resp.media = next_events


handlers = media.Handlers({
    'application/json': jsonhandler.JSONHandler(),
})

app = falcon.API()

app.req_options.media_handlers = handlers
app.resp_options.media_handlers = handlers

app.add_route('/events/', EventsResource())
