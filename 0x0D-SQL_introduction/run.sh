#!/bin/bash

# Loop through all .sql files in the current directory
for file in *.sql; do
    # Exclude the file "run.sql"
    if [ "$file" != "run.sql" ]; then
        echo "Running $file..."
        mysql -h localhost -u root -p < 26120
    fi
done
