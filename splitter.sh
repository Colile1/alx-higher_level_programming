#!/bin/bash

# Define the file location
file_location="0x03-python-data_structures"

# Input C file name
input_file="13-is_palindrome.c"

# Navigate to the directory containing the C file
cd "$file_location" || exit

# Create a directory to store individual function files
mkdir -p function_files

# Temporary variable to store the current function content
current_function=""
next_function_name=""

# Function to save the content of the current function to a file
save_function() {
    local function_content="$1"
    echo "$function_content" > "function_files/$2.c"
}

# Read the input file line by line
while IFS= read -r line; do
    if [[ $line == "/**" ]]; then
        # Save the previous function content to a file
        if [[ -n $current_function ]]; then
            save_function "$current_function" "$next_function_name"
            current_function=""
        fi
        current_function="$line\n"
    elif [[ -n $current_function ]]; then
        current_function+="$line\n"
        # Capture the function name after `/**` as the filename
        if [[ $line =~ \* ]]; then
            next_function_name=$(echo "$line" | awk -F'[* ]+' 'NF>2{print $3; exit}')
        fi
    fi
done < "$input_file"

# Save the last function content to a file
if [[ -n $current_function ]]; then
    save_function "$current_function" "$next_function_name"
fi

echo "Functions split into separate files in 'function_files' directory."
