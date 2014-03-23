import pytumblr
import secret
import time
import calendar

consumer = 'h93vg3vWvfWJKloahZ6EoJzVwv9D2FhORp3degELUdk4WK6puF'
app  = 'OLXURhKe7gUw8dE1A142VQjHDYoxNDMGHYncQSGHiL5eoxGq4v'

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer,
    secret.tumblr_consumer,
    app,
    secret.tumblr_app,
    )

def process_post(post):
    out = {}
    # timestamp will be stored in seconds since the epoch
    out["timestamp"] = post["timestamp"]
    post_type = post["type"]
    # text, quote, link, answer, video, audio, photo, chat
    if post_type == "photo" or post_type == "video" or post_type == "audio":
        text = post["caption"]
    elif post_type == "text" or post_type == "chat":
        text = post["body"]
    elif post_type == "quote":
        text = post["text"]
    elif post_type == "link":
        text = post["description"]
    elif post_type == "answer":
        text = post["answer"]
        
    out["text"] = text
    out["url"] = post["post_url"] # for reference
    return out
    
# returns an array of formatted posts
# from day of timestamp in UTC, no DST
def get_posts(month, day, year, tag="lol"):
    end_struct = time.struct_time((year, month, day, 23, 59, 59, 0, 0, 0))
    end = calendar.timegm(end_struct)
    begin_struct = time.struct_time((year,month,day,0,0,0,0,0,0))
    begin = calendar.timegm(begin_struct)
    response = client.tagged(tag, filter="text", before=end)
    within_day = [item for item in response if item["timestamp"] >= begin]
    out = [process_post(post) for post in within_day]
    return out
