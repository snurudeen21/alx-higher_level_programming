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

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        response_json = response.json()
        if not response_json:
            print("No result")
        else:
            print("[{}] {}".format(response_json.get('id'), response_json.get('name')))

    except Exception:
        print("Not a valid JSON")