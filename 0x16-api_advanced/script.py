#!/usr/bin/python3

from fake_useragent import UserAgent

def get_random_user_agent():
    """
    Function to get a random user-agent string.

    Returns:
        str: A random user-agent string.
    """
    user_agent = UserAgent()
    return user_agent.random

# Example usage:
random_user_agent = get_random_user_agent()
print(f"Random User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62")
