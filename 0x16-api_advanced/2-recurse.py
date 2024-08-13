#!/usr/bin/python3

"""
Function that recursively queries the Reddit API and returns
a list of titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively returns a list of titles of all hot articles
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of hot article titles. Defaults to an empty list.
        after (str): The "after" key for pagination. Defaults to None.
    
    Returns:
        list: List of titles of hot articles, or None if no results found.
    """
    usr = {"User-Agent": "lizzie"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=usr, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    after = data.get("after")
    children = data.get("children", [])

    if not children and not after:
        return hot_list if hot_list else None

    hot_list.extend([post.get("data").get("title") for post in children])

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


