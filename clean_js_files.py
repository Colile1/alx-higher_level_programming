#!/usr/bin/python3
import os

def clean_js_files():
    # Get all .js files in current directory
    js_files = [f for f in os.listdir('.') if f.endswith('.js')]
    
    for js_file in js_files:
        # Read file content
        with open(js_file, 'r') as file:
            lines = file.readlines()
        
        # Clean lines: remove trailing spaces and empty lines
        cleaned_lines = [line.rstrip() for line in lines if line.strip()]
        
        # Write back to file with final newline
        with open(js_file, 'w') as file:
            file.write('\n'.join(cleaned_lines) + '\n')
        print(f"Cleaned: {js_file}")

if __name__ == "__main__":
    clean_js_files()
