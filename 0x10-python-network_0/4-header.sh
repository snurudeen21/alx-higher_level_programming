#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET
curl -s --header "X-School-User-Id:98" "$1"
