#!/usr/bin/python3

"""
Function that queries the Reddit API and prints the 
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        None
    """
    usr = {"User-Agent": "custom-user-agent"}
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    response = requests.get(url, headers=usr, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")

