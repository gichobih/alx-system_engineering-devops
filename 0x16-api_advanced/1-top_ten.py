#!/usr/bin/python3

"""
function that queries the Reddit API and prints the 
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests
from sys import argv

def top_ten(subreddit):

   """
   Returns top ten posts from a given subreddit.
   """
   usr = {"User-Agent": "lizzie"}
   url = requests.get(
           "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit),
           headers = usr,
           allow_redirect= False
    ).json()

   try:
       for post in url.get("data").get("children"):
           print(post.get("data").get("title"))
   except (KeyError, TypeError):
       print("None")


if __name__ == "__main__":
    top_ten(argv[1])
