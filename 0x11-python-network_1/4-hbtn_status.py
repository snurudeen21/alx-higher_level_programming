#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status

-You must use the package requests
-You are not allow to import packages other than requests
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    response = response.text

    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
