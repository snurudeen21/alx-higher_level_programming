#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]  # username
    repo = sys.argv[2]  # repo name

    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    r = requests.get(url)
    for com in r.json()[:10]:
        print("{}: {}".format(com['sha'], com['commit']['author']['name']))
