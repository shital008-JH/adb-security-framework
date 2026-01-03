import json
from datetime import datetime
from modules.trust_filter_engine_v1 import apply_trust_filter

def generate_report():
    data = apply_trust_filter()
    report = {
        "generated_at": str(datetime.now()),
        "total_apps_analyzed": len(data),
        "high_risk_apps": [a for a in data if a["final_score"] >= 70],
        "all_results": data
    }
    return report

def save_report(path="reports/security_report.json"):
    report = generate_report()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    return path
