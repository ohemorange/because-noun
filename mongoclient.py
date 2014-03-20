# usage
# import mongoclient
# insert_post(post)
# post should be formatted
# this does no processing of post
# just inserts into the db

from pymongo import MongoClient

# startup connection to db
client = MongoClient()
db = client.post_db
posts = db.posts

# insert post into db
def insert_post(post):
   post_id = posts.insert(post)
   return post_id

 
