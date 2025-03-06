#!/bin/bash
# Sends a GET request to a URL and displays the body if the status code is 200
output=$(curl -s -w "\n%{http_code}" "$1") && status="${output##*$'\n'}" && body="${output%$'\n'*}" && [ "$status" -eq 200 ] && printf "%s" "$body"