#!/usr/bin/python3
import ast
import subprocess

def get_imports(file_path):
    with open(file_path, 'r') as file:
        root = ast.parse(file.read())
    
    imports = set()
    for node in ast.walk(root):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def install_dependencies(file_path):
    imports = get_imports(file_path)
    standard_libs = set(['os', 'sys', 'time', 'datetime', 'math', 'random', 'json', 're'])
    
    packages_to_install = imports - standard_libs
    
    for package in packages_to_install:
        print(f"Installing {package}...")
        subprocess.run(['pip', 'install', package], shell=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        install_dependencies(sys.argv[1])
    else:
        print("Please provide a Python file path")
