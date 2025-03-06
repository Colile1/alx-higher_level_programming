#!/bin/bash
# This script sends a GET request and displays the body only if the status code is 200.

response=$(curl -s -w "\n%{http_code}" "$1")
status_code=$(echo "$response" | tail -n 1)
body=$(echo "$response" | head -n -1)

if [ "$status_code" -eq 200 ]; then
    printf "%s" "$body"
fi