#!/usr/bin/python3
"""
Module to query the Reddit API and return a list containing the titles
of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to fetch titles of all hot articles for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): Token indicating the starting point for pagination.

    Returns:
        list or None: List containing titles of hot articles, or None if no results found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
    headers = {"User-Agent": custom_user_agent}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404 Not Found)
        data = response.json()

        # Check if the subreddit is valid and has posts
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in posts])

            # Check if there are more pages to fetch
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None  # Invalid subreddit or no posts
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return None
        else:
            print(f"Error: {e}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
