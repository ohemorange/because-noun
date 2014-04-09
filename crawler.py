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
    a = date(2007, 3, 1)
    b = date(2013, 12, 31) # 2014, 3, 22

    for dt in rrule(DAILY, dtstart=a, until=b):
        if dt.day == 1 and dt.month == 1:
            print dt.year
        posts = tumblr.get_posts(dt.month,
                                 dt.day,
                                 dt.year)
        mongoclient.insert_posts(posts)

crawl_tumblr()
