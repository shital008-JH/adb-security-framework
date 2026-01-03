import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from modules.logcat_analyzer_v1 import analyze_logcat
from modules.device_info import device_connected

def run():
    print("\n📜 Logcat & Crash Analyzer v1\n")

    if not device_connected():
        print("❌ No device connected.")
        return

    full_log, error_log, error_count = analyze_logcat()

    print("✅ Log capture complete")
    print("📄 Full log saved at:", full_log)
    print("🚨 Error log saved at:", error_log)
    print(f"⚠️ Total errors detected: {error_count}")

if __name__ == "__main__":
    run()
