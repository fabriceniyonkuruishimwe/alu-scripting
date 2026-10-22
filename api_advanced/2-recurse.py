#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts of a subreddit.

    Returns None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        data = response.json()["data"]
        posts = data["children"]
    except (requests.RequestException, ValueError, KeyError, TypeError):
        return None

    for post in posts:
        hot_list.append(post["data"]["title"])

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
