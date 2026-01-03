import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from modules.log_classifier_v1 import (
    fetch_logcat,
    classify_logs,
    save_classification_report,
    get_severity_verdict
)
from modules.device_info import device_connected

def run():
    print("\n🧠 Smart Log Classification Engine v1\n")

    if not device_connected():
        print("❌ No device connected.")
        return

    logs = fetch_logcat()
    classified = classify_logs(logs)

    for k, v in classified.items():
        print(f"{k}: {len(v)}")

    verdict = get_severity_verdict(classified)
    report = save_classification_report(classified)

    print("\n📊 Severity Verdict:", verdict)
    print("📁 Report saved at:", report)

if __name__ == "__main__":
    run()
