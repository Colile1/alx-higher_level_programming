#!/usr/bin/python3
import os

def add_space_to_js_files():
    # Get all .js files in current directory
    js_files = [f for f in os.listdir('.') if f.endswith('.js')]
    
    for js_file in js_files:
        # Read file content
        with open(js_file, 'r') as file:
            lines = file.readlines()
        
        # Add space at the end of each line if not already present
        modified_lines = [line.rstrip() + ' \n' for line in lines]
        
        # Write back to file
        with open(js_file, 'w') as file:
            file.writelines(modified_lines)
        print(f"Processed: {js_file}")

if __name__ == "__main__":
    add_space_to_js_files()
