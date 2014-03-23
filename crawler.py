import tumblr
from datetime import date
from dateutil.rrule import rrule, DAILY
import mongoclient

CRAWL_TUMBLR = True

# grabs at most 20 posts a day with tag lol
# from tumblr and stores them in the database
def crawl_tumblr():
    if not CRAWL_TUMBLR:
        return
    # date incrementing code from stackoverflow
    # a = date(2007, 3, 1)
    a = date(2014, 1, 1) # starting with 2014 as a test
    b = date(2014, 3, 22)

    for dt in rrule(DAILY, dtstart=a, until=b):
        posts = tumblr.get_posts(dt.date.month,
                                 dt.date.day,
                                 dt.date.year)
        mongoclient.insert_posts(posts)

crawl_tumblr()
