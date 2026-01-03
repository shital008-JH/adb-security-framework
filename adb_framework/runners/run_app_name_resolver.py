import sys, os, json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.app_name_resolver import get_app_name

REPORT_PATH = "reports/security_report.json"

print("\n🔤 App Name Resolution Engine\n")

with open(REPORT_PATH, "r", encoding="utf-8") as f:
    report = json.load(f)

for app in report["all_results"][:10]:
    name = get_app_name(app["package"])
    print(f"{app['package']}  →  {name}")
