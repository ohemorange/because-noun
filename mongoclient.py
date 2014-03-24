# usage
# import mongoclient
# insert_post(post)
# post should be formatted
# this does no processing of post
# just inserts into the db

from pymongo import MongoClient
from datelib import *

# startup connection to db
client = MongoClient()
db = client.post_db
posts = db.posts

# insert post into db
def insert_post(post):
   post_id = posts.insert(post)
   return post_id

# insert all posts in a list into db
def insert_posts(posts):
   for post in posts:
      insert_post(post)

def get_posts_from_day(month, day, year):
   end = end_timestamp(month, day, year)
   begin = begin_timestamp(month, day, year)
   day_posts = posts.find({"timestamp":{"$gt":begin, "$lt":end}})
   return day_posts
      
def map(function):
   all = list(posts.find())
   for post in all:
      function(post)
      posts.save(post)

# must take post as only parameter
def sample_function(post):
   post["origin"] = "tumblr"

def sample_map():
   map(sample_function)
