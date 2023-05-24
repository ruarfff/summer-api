import os

from pynytimes import NYTAPI

# Load our API key from the environment
# You must get the API key from https://developer.nytimes.com/get-started
API_KEY = os.getenv("NYTIMES_API_KEY", "")
nyt = NYTAPI(API_KEY, parse_dates=True)


def get_top_stories():
    return nyt.top_stories()
