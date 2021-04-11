#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). Also manages
urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
