from adb_utils import run_adb
from datetime import datetime
import os

CRITICAL_KEYWORDS = [
    "FATAL EXCEPTION",
    "ANR in",
    "Process has died",
    "SIGSEGV"
]

RECOVERABLE_KEYWORDS = [
    "system_server",
    "ServiceManager",
    "watchdog",
    "Binder",
    "Timeout"
]

VENDOR_KEYWORDS = [
    "Oplus",
    "Oppo",
    "Qualcomm",
    "Modem",
    "thermal",
    "horae",
    "crashbox"
]

def fetch_logcat(lines=300):
    return run_adb(["logcat", "-d", "-t", str(lines)])

def classify_logs(logs):
    classification = {
        "CRITICAL": [],
        "RECOVERABLE": [],
        "VENDOR_NOISE": [],
        "UNCATEGORIZED": []
    }

    for line in logs.splitlines():
        upper = line.upper()

        if any(k in upper for k in CRITICAL_KEYWORDS):
            classification["CRITICAL"].append(line)
        elif any(k.upper() in upper for k in RECOVERABLE_KEYWORDS):
            classification["RECOVERABLE"].append(line)
        elif any(k.upper() in upper for k in VENDOR_KEYWORDS):
            classification["VENDOR_NOISE"].append(line)
        elif " E " in line:
            classification["UNCATEGORIZED"].append(line)

    return classification

def save_classification_report(data):
    os.makedirs("reports/log_classification", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"reports/log_classification/log_classification_{ts}.txt"

    with open(path, "w", encoding="utf-8") as f:
        for category, logs in data.items():
            f.write(f"\n===== {category} ({len(logs)}) =====\n")
            for line in logs[:20]:
                f.write(line + "\n")

    return path

def get_severity_verdict(classified):
    if len(classified["CRITICAL"]) > 0:
        return "🔴 CRITICAL RISK"
    if len(classified["RECOVERABLE"]) > 20:
        return "🟠 MODERATE RISK"
    return "🟢 LOW RISK"
