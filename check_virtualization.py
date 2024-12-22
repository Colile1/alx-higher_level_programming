#!/usr/bin/python3
import subprocess
import sys

def check_virtualization():
    # Check if virtualization is enabled
    try:
        result = subprocess.run(['systeminfo'], capture_output=True, text=True)
        if "Virtualization Enabled In Firmware: Yes" in result.stdout:
            print("✅ Virtualization is enabled in BIOS")
        else:
            print("❌ Virtualization needs to be enabled in BIOS")
            print("Steps to enable in BIOS:")
            print("1. Restart PC and enter BIOS (usually F2, F12, or Del key)")
            print("2. Look for Virtualization Technology (VT-x/AMD-V)")
            print("3. Enable it")
            print("4. Save and restart")
    except Exception as e:
        print(f"Error checking virtualization: {e}")

def enable_virtual_machine_platform():
    try:
        # Enable Virtual Machine Platform
        subprocess.run(['powershell', 'Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart'], check=True)
        print("✅ Virtual Machine Platform enabled successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to enable Virtual Machine Platform")
        print("Try enabling manually through Windows Features")

if __name__ == "__main__":
    print("Checking system configuration...")
    check_virtualization()
    enable_virtual_machine_platform()