#!/bin/bash
# This script sends a GET request and displays the body only if the status code is 200.

curl -s "$1" -o /tmp/body && [ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" -eq 200 ] && cat /tmp/body
