from because_lib import *
import mongoclient as m
import sys

START = 0
END = 30

def pbc_count(start, end):
    bc_posts = m.posts.find({'text': {'$regex':'.*because.*', '$options':'is'}})
    pbc_posts = [post for post in bc_posts[start:end] if has_because(post["text"])]
    return len(pbc_posts)

if len(sys.argv) < 3:
    start = START
    end = END
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

print pbc_count(start, end)
