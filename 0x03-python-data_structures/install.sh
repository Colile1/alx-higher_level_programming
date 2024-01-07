#!/bin/bash

# Update package lists
sudo apt-get update

# Install essential build tools (gcc, make)
sudo apt-get install -y build-essential

# Install Python development files
sudo apt-get install -y python3-dev

# Compile the C file into a shared library
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
