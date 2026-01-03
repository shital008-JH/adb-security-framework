import sys
import os
import time

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from modules.automation_engine_v1 import (
    tap,
    swipe,
    take_screenshot
)
from modules.device_info import device_connected

def run():
    print("\n🤖 Automation Engine v1\n")

    if not device_connected():
        print("❌ No device connected.")
        return

    print("📸 Taking screenshot...")
    shot = take_screenshot()
    print("Saved:", shot)

    print("\n👉 Performing tap (center screen)...")
    tap(500, 1200)
    time.sleep(1)

    print("👉 Performing swipe...")
    swipe(500, 1400, 500, 400)

    print("\n✅ Automation demo completed")

if __name__ == "__main__":
    run()
