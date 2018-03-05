import feedparser
from datetime import datetime

class Client(object):

    def __init__(self, url):
        self.url = url
        self.__load()

    def __load(self):
        self.feed = feedparser.parse(self.url)

    def metadata(self):
        """
        Returns meta information from the feed
        """
        return {
            "title": self.feed["feed"].get("title"),
            "link": self.feed["feed"].get("link"),
            "description": self.feed["feed"].get("description"),
            "published": self.feed["feed"].get("published"),
        }

    def __entry_details(self, entry):
        """
        Returns only a few entry details we care about
        """
        return {
            "title": entry["title"],
            "summary": entry["summary"],
            "link": entry["link"],
            "published": datetime(
                entry["published_parsed"][0], entry["published_parsed"][1], entry["published_parsed"][2],
                entry["published_parsed"][3], entry["published_parsed"][4], entry["published_parsed"][5]
            )
        }

    def recent_items(self, num=3):
        """
        Returns the num most recent entries from the feed
        """
        out = []
        for n in range(0, num):
            out.append(self.__entry_details(self.feed.entries[n]))
        return out
