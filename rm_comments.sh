#!/bin/bash

# Navigate to the directory containing the Python files
cd 0x03-python-data_structures

# Loop through each .py file in the directory
for file in *.c; do
    # Remove Python comments from the file
    sed -i '/^\s*#/d;/^\s*$/d' "$file"
    # Remove C-style single-line comments from the file
    sed -i '/^\s*\/\//d' "$file"
    echo "Comments removed from $file"
done

chmod +x *
