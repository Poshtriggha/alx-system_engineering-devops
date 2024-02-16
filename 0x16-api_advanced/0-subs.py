#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    try:
        results = response.json()["data"]
        return results["subscribers"]
    except KeyError:
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
