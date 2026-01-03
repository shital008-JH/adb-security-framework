import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from modules.permission_risk_engine_v1 import analyze_permission_risk
from modules.device_info import device_connected

def run():
    print("\n🔐 Permission Abuse & Privacy Risk Engine v1\n")

    if not device_connected():
        print("❌ No device connected.")
        return

    results = analyze_permission_risk()

    if not results:
        print("✅ No high-risk permissions detected.")
        return

    for app in results[:5]:
        print("=" * 60)
        print("Package:", app["package"])
        print("Dangerous Permissions:")
        for p in app["dangerous_permissions"]:
            print(" -", p)
        print("Risk Score:", app["risk_score"])

    print(f"\n⚠️ Total risky apps detected: {len(results)}")

if __name__ == "__main__":
    run()
