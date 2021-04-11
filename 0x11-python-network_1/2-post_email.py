#!/usr/bin/python3
""" A script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
