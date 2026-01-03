from adb_utils import run_adb
import os
from datetime import datetime

def tap(x, y):
    return run_adb(["shell", "input", "tap", str(x), str(y)])

def swipe(x1, y1, x2, y2, duration=300):
    return run_adb([
        "shell", "input", "swipe",
        str(x1), str(y1), str(x2), str(y2), str(duration)
    ])

def take_screenshot():
    os.makedirs("reports/screenshots", exist_ok=True)
    filename = f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    device_path = "/sdcard/temp_screen.png"

    run_adb(["shell", "screencap", "-p", device_path])
    run_adb(["pull", device_path, f"reports/screenshots/{filename}"])
    run_adb(["shell", "rm", device_path])

    return filename
