#!/usr/bin/python3
import json
import os

def set_ubuntu_default():
    # Get VS Code settings file path
    settings_path = os.path.expanduser("~/AppData/Roaming/Code/User/settings.json")
    
    # Create settings if they don't exist
    if not os.path.exists(settings_path):
        os.makedirs(os.path.dirname(settings_path), exist_ok=True)
        default_settings = {}
    else:
        with open(settings_path, 'r') as f:
            default_settings = json.load(f)
    
    # Update terminal settings
    terminal_settings = {
        "terminal.integrated.defaultProfile.windows": "Ubuntu",
        "terminal.integrated.profiles.windows": {
            "Ubuntu": {
                "path": "wsl.exe",
                "args": ["-d", "Ubuntu"],
                "icon": "terminal-ubuntu"
            }
        }
    }
    
    # Update settings
    default_settings.update(terminal_settings)
    
    # Save updated settings
    with open(settings_path, 'w') as f:
        json.dump(default_settings, f, indent=4)
    
    print("✅ Ubuntu set as default terminal in VS Code!")

if __name__ == "__main__":
    set_ubuntu_default()
