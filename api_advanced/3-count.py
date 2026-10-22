#!/usr/bin/python3
"""Module that recursively counts keywords in the titles of hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Prints nothing if the subreddit is invalid or no keywords match.
    """
    if counts is None:
        counts = {}

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
        return

    for post in posts:
        for word in post["data"]["title"].lower().split():
            counts[word] = counts.get(word, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    totals = {}
    for word in word_list:
        word = word.lower()
        if word in counts:
            totals[word] = totals.get(word, 0) + counts[word]

    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
