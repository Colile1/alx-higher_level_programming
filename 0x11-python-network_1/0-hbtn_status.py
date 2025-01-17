#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def fetch():
    url_ = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url_) as response:
        body = response.read()
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch()
