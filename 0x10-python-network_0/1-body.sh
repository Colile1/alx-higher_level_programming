#!/bin/bash
# This script sends a GET request and displays the body only if the status code is 200.
if [ "$#" -ne 1 ]; then
    exit 1
fi

response=$(curl -s -w "%{http_code}" "$1")

status="${response: -3}"
body="${response::-3}"

if [ "$status" -eq 200 ]; then
    echo "$body"
fi
