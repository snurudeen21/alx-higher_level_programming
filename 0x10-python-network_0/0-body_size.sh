#!/bin/bash
# use to curl to send request to a url and recieve in byte
curl -s "$1" | wc -c
