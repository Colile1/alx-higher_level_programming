#!/bin/bash
# This is a bash code that runs all the files in the current file and all sub files
shopt -s globstar

for file in **; do
  if [ -f "$file" ]; then
    bash "$file"
  fi
done
