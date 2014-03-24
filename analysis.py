from because_lib import *

import mongoclient as m

def pbc_count():
    bc_posts = m.posts.find({'text': {'$regex':'.*because.*', '$options':'is'}})
    pbc_posts = [post for post in bc_posts if has_because(post["text"])]
    print len(pbc_posts)

