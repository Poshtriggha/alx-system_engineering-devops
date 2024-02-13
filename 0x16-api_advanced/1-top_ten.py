#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests
from fake_useragent import UserAgent

def get_random_user_agent():
    """
    Function to get a random user-agent string.

    Returns:
        str: A random user-agent string.
    """
    # Add your custom user agent
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
    
    # Use the custom user agent if available, otherwise generate a random one
    user_agent = UserAgent(use_cache_server=False, verify_ssl=False)
    return custom_user_agent if custom_user_agent else user_agent.random

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": get_random_user_agent()}  # Use a random or custom user-agent to avoid Too Many Requests errors

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404 Not Found)
        data = response.json()
        subscribers_count = data["data"]["subscribers"]
        return subscribers_count
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print(f"Error: {e}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit)
        print("{:d}".format(subscribers_count))
