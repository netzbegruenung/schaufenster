import six

from datetime import date, datetime

from falcon import errors
from falcon.media import BaseHandler
from falcon.util import json

class ComplexEncoder(json.JSONEncoder):

    """JSONENcoder that handles date and datetime"""

    def default(self, obj):
        if isinstance(obj, date) or isinstance(obj, datetime):
            return obj.isoformat()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class JSONHandler(BaseHandler):
    """Handler built using Python's :py:mod:`json` module."""

    def deserialize(self, raw):
        try:
            return json.loads(raw.decode('utf-8'))
        except ValueError as err:
            raise errors.HTTPBadRequest(
                'Invalid JSON',
                'Could not parse JSON body - {0}'.format(err)
            )

    def serialize(self, media):
        result = json.dumps(media,
                            ensure_ascii=False,
                            cls=ComplexEncoder)
        if six.PY3 or not isinstance(result, bytes):
            return result.encode('utf-8')

        return result
