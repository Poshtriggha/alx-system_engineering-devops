#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Function to print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"}  # Add a custom User-Agent to avoid Too Many Requests errors

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404 Not Found)
        data = response.json()

        # Check if the subreddit is valid and has posts
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children'][:10]  # Get the first 10 posts
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")  # Invalid subreddit or no posts
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
