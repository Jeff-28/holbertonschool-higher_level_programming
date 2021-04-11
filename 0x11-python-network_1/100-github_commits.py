#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
You must use the GitHub API, here is the documentation
    https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
A Python script that takes 2 arguments in order to solve this challenge:
    The first argument will be the repository name
    The second argument will be the owner name
"""

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    data = r.json()
    try:
        for j in range(10):
            print('{}: {}'.format(data[j].get('sha'),
                                  data[j].get('commit')
                                  .get('author').get('name')))
    except:
        pass
