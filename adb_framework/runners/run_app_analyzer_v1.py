import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from modules.app_analyzer_v1 import (
    list_packages,
    get_basic_app_info,
    get_permissions_summary
)
from modules.device_info import device_connected

def run():
    print("\n📊 App Analyzer v1 (Read-Only)\n")

    if not device_connected():
        print("❌ No device detected.")
        return

    packages = list_packages()
    print(f"Total installed apps: {len(packages)}\n")

    for pkg in packages[:3]:
        print("=" * 60)
        info = get_basic_app_info(pkg)
        print("Package:", info["package"])
        print("APK Path:", info["apk_path"])
        print("Installer:", info["installer"])

        print("\nPermissions (sample):")
        perms = get_permissions_summary(pkg)
        if perms:
            for p in perms:
                print(" ", p)
        else:
            print("  None detected")

if __name__ == "__main__":
    run()
