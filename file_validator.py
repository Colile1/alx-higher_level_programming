#!/usr/bin/python3
import os
import stat
import subprocess

def ensure_requirements():
    # Install semistandard if not present
    try:
        subprocess.run(['npm', 'install', 'semistandard@16'], check=True)
    except subprocess.CalledProcessError:
        print("Installing semistandard...")
        subprocess.run(['npm', 'install', '-g', 'semistandard@16'])

    # Create README.md if not exists
    if not os.path.exists('README.md'):
        with open('README.md', 'w') as f:
            f.write('# Project Name\nDescription of your project goes here.\n')
        print("✅ Created README.md")

    # Process all .js files
    for filename in os.listdir('.'):
        if filename.endswith('.js'):
            fix_file(filename)

def fix_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.splitlines()

    changes_made = False
    new_content = []

    # Check shebang
    if not lines or lines[0] != '#!/usr/bin/node':
        new_content.append('#!/usr/bin/node')
        changes_made = True
    
    # Add original content
    new_content.extend(lines[1:] if lines else [])

    # Ensure ending newline
    if not content.endswith('\n'):
        new_content.append('')
        changes_made = True

    if changes_made:
        with open(filename, 'w') as f:
            f.write('\n'.join(new_content) + '\n')
        print(f"✅ Fixed {filename}")

    # Make file executable
    current_mode = os.stat(filename).st_mode
    os.chmod(filename, current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # Run semistandard
    try:
        subprocess.run(['npx', 'semistandard', '--fix', filename])
        print(f"✅ Applied semistandard to {filename}")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Semistandard found issues in {filename}")

if __name__ == "__main__":
    ensure_requirements()
    print("✅ All files processed successfully!")
