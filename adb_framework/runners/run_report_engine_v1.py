import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.report_engine_v1 import save_report
from modules.device_info import device_connected

print("\n📊 Unified Security Report Generator v1\n")

if not device_connected():
    print("❌ No device connected.")
    exit()

path = save_report()
print("✅ Report generated at:", path)
