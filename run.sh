#!/bin/bash

shopt -s globstar

for file in **; do
  if [ -f "$file" ]; then
    bash "$file"
  fi
done
