#!/usr/bin/python3
"""
Module to query the Reddit API, parse the title of all hot articles,
and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursive function to count occurrences of keywords in the titles of hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): Token indicating the starting point for pagination.
        count_dict (dict): Dictionary to store the counts.

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
    headers = {"User-Agent": custom_user_agent}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                for keyword in word_list:
                    keyword = keyword.lower()
                    if keyword in title:
                        count_dict[keyword] = count_dict.get(keyword, 0) + 1

            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, count_dict)
            else:
                print_results(count_dict)
        else:
            print("Invalid subreddit or no posts.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def print_results(count_dict):
    """
    Function to print the sorted count of keywords.

    Args:
        count_dict (dict): Dictionary containing the counts.

    Returns:
        None
    """
    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_items:
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x for x in sys.argv[2].split()]
        count_words(subreddit, word_list)

