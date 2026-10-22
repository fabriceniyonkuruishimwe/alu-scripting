#!/usr/bin/python3
"""Module that queries the Reddit API for subscriber counts."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit.

    Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/student)"}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        return response.json()["data"]["subscribers"]
    except (requests.RequestException, ValueError, KeyError, TypeError):
        return 0
