#!/usr/bin/python3
import ast
import os
import re

class VariableFinder(ast.NodeVisitor):
    def __init__(self):
        self.variables = {}
        self.current_file = ""

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            if self.current_file not in self.variables:
                self.variables[self.current_file] = set()
            self.variables[self.current_file].add(node.id)
        self.generic_visit(node)

def find_variables_in_files():
    finder = VariableFinder()
    
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    finder.current_file = file_path
                    tree = ast.parse(content)
                    finder.visit(tree)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return finder.variables

def replace_variable(file_path, old_name, new_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace variable while preserving case and avoiding partial matches
    pattern = r'\b' + re.escape(old_name) + r'\b'
    modified_content = re.sub(pattern, new_name, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

def main():
    variables = find_variables_in_files()
    
    # Display all variables by file
    for file_path, vars_set in variables.items():
        print(f"\nFile: {file_path}")
        for i, var in enumerate(vars_set, 1):
            print(f"{i}. {var}")
    
    # Variable replacement interface
    while True:
        choice = input("\nWould you like to rename a variable? (yes/no): ").lower()
        if choice != 'yes':
            break
            
        file_path = input("Enter the file path: ")
        if file_path not in variables:
            print("File not found!")
            continue
            
        old_name = input("Enter the variable name to replace: ")
        if old_name not in variables[file_path]:
            print("Variable not found in this file!")
            continue
            
        new_name = input("Enter the new variable name: ")
        replace_variable(file_path, old_name, new_name)
        print(f"Variable '{old_name}' replaced with '{new_name}' in {file_path}")

if __name__ == "__main__":
    main()
