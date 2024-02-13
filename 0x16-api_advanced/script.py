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
print(f"Random User-Agent: {random_user_agent}")
