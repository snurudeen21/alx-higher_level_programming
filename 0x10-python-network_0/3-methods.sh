#!/bin/bash
# send a request to webserve to display all the METHODS allowed
curl -s -I "$1" | grep "Allow:" | cut -d " " -f 2-
