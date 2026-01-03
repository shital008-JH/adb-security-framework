import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.trust_filter_engine_v1 import apply_trust_filter
from modules.device_info import device_connected

print("\n🧠 Trust-Aware Risk Filter Engine v1\n")

if not device_connected():
    print("❌ No device connected.")
    exit()

results = apply_trust_filter()

for app in sorted(results, key=lambda x: x["final_score"], reverse=True)[:5]:
    print("="*60)
    print("Package:", app["package"])
    print("Trust Level:", app["trust_level"])
    print("Original Risk:", app["original_score"])
    print("Final Risk:", app["final_score"])
