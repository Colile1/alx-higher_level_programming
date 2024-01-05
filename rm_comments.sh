#!/bin/bash

# Navigate to the directory containing the Python files
cd 0x03-python-data_structures

# Loop through each .py file in the directory
for file in *.py; do
    # Remove comments from the Python file
    sed -i '/^\s*#/d;/^\s*$/d' "$file"
    echo "Comments removed from $file"
done
