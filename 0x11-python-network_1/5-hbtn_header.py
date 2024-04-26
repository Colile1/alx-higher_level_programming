#!/usr/bin/python3
"""
takes in URL, sends a request to the URL and displays the
X-Request-Id variable found in the header of the response.
"""
import requests
from sys import argv


def request_idr():
    """
    Displays the value of the X-Request-Id variable
    """
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == "__main__":
    request_idr()
