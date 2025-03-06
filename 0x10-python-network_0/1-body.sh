#!/bin/bash
# This script sends a GET request and displays the body only if the status code is 200.
c=$(curl -sL -w "%{http_code}" "$1"); code=${c: -3}; [ "$code" -eq 200 ] && echo "${c::-3}"