import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.device_info import (
    device_connected,
    get_device_info,
    save_report
)

def run():
    print("\n🔍 Running Device Intelligence Engine...\n")

    if not device_connected():
        print("❌ No authorized Android device detected.")
        return

    info = get_device_info()

    print("📱 DEVICE SUMMARY")
    print("-" * 45)
    for k, v in info.items():
        print(f"{k}:\n{v}")
        print("-" * 45)

    report = save_report(info)
    print(f"\n📁 Report saved at: {report}")

if __name__ == "__main__":
    run()
