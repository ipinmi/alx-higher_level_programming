#!/usr/bin/python3
"""
    Sends a request to a given URL and displays the response body.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
