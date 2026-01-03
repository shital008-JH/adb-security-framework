import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from modules.security_audit_v1 import (
    run_security_audit,
    calculate_risk_score
)
from modules.device_info import device_connected

def run():
    print("\n🛡️ Android Security Audit v1\n")

    if not device_connected():
        print("❌ No device connected.")
        return

    findings = run_security_audit()

    for k, v in findings.items():
        print(f"{k}: {v}")

    score = calculate_risk_score(findings)

    print("\n⚠️ Risk Score:", score, "/ 100")

    if score >= 70:
        print("❗ High Risk Device")
    elif score >= 40:
        print("⚠️ Medium Risk Device")
    else:
        print("✅ Low Risk Device")

if __name__ == "__main__":
    run()
