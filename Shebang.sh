#!/bin/bash

# Navigate to the directory containing the Python files
#cd /mnt/c/Users/enigm/OneDrive/Documents/school/ALX/Software-Engineering/5_Python/alx-higher_level_programming/0x02-python-import_modules#
cd 0x03-python-data_structures

# Loop through each .py file in the directory
for file in *.py; do
    # Check if the file doesn't start with the shebang line
    if [[ $(pnt_hd -n 1 "$file") != "#!/usr/bin/python3" ]]; then
        # Prepend the shebang line to the file
        echo "#!/usr/bin/python3" | cat - "$file" > temp && mv temp "$file"
        echo "Added shebang to $file"
    else
        echo "Shebang already exists in $file"
    fi
done

chmod +x *
