from adb_utils import run_adb
import os
from datetime import datetime

def capture_logcat(lines=200):
    output = run_adb(["logcat", "-d", f"-t", str(lines)])
    return output

def filter_errors(logs):
    return [
        line for line in logs.splitlines()
        if " E " in line or " FATAL " in line
    ]

def save_log_report(content, filename):
    os.makedirs("reports/logs", exist_ok=True)
    path = f"reports/logs/{filename}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path

def analyze_logcat():
    logs = capture_logcat()
    errors = filter_errors(logs)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_log = save_log_report(logs, f"logcat_full_{timestamp}.txt")
    error_log = save_log_report(
        "\n".join(errors),
        f"logcat_errors_{timestamp}.txt"
    )

    return full_log, error_log, len(errors)
