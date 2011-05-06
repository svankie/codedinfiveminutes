__author__ = 'Horacio Bertorello'

from collections import namedtuple
import feedparser

PERMITTED_FIELDS = ["title", "summary", "link"]
Job = namedtuple('Job', " ".join(PERMITTED_FIELDS))

FEEDS = ["http://www.zonajobs.com.ar/empleos/Java?format=rss"]

class Parser(object):
    """
        A simple parser.
    """
    def __init__(self, feeds):
        if not feeds:
            raise Exception("Epa. Dame feeds.")
	self.feeds = feeds

    def parse(self):
	jobs = set()
	for feed in self.feeds:
            data = feedparser.parse(feed)
            for datum in data.entries:
                job = Job(*[v for k,v in datum.items() if k in PERMITTED_FIELDS])
	        jobs.add(job)
        return jobs

if __name__ == '__main__':
    parser = Parser(FEEDS)
    res = parser.parse()
    
    for item in res:
        print item

