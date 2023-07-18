#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
-If no argument is given, set q=""
-If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
"""
import sys
import requests


if __name__ == "__main__":
    data = {}

    if len(sys.argv) == 1:
        data['q'] = ""
    else:
        data['q'] = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        r_json = r.json()
        if not r_json:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))

    except Exception:
        print("Not a valid JSON")
