#!/bin/bash

# Specify the path to your Git repository
repo_path="/0x04-python-more_data_structures"

# Navigate to the Git repository directory
cd "$repo_path"

# Increment the version number
version=$(git rev-list --count HEAD)
((version++))

# Add all changes
git add .

# Commit changes with an auto-incremented version number
commit_message="git auto update number: $version"
git commit -m "$commit_message"

# Push changes to the remote repository
git push origin master
