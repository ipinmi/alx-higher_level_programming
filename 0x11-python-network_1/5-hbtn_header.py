#!/usr/bin/python3
"""
    displays the value of the X-Request-Id variable
    found in the header of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    print(request.headers.get("X-Request-Id"))
