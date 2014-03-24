from because_lib import *

import mongoclient as m

def pbc_count():
    bc_posts = m.posts.find({'text': {'$regex':'.*because.*', '$options':'is'}})
    pbc_posts = [post for post in bc_posts if has_because(post["text"])]
    return len(pbc_posts)

print pbc_count()
