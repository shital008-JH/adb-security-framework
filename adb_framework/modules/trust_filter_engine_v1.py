from modules.permission_risk_engine_v1 import analyze_permission_risk
from adb_utils import run_adb

OEM_KEYWORDS = ["oplus", "realme", "coloros", "miui", "samsung", "mediatek"]

def classify_app(package):
    if package.startswith("com.android") or package.startswith("com.google"):
        return "SYSTEM"
    for k in OEM_KEYWORDS:
        if k in package.lower():
            return "OEM"
    return "USER"

def adjust_risk(score, trust):
    if trust == "SYSTEM":
        return int(score * 0.3)
    if trust == "OEM":
        return int(score * 0.6)
    return score

def apply_trust_filter():
    raw = analyze_permission_risk()
    refined = []

    for app in raw:
        trust = classify_app(app["package"])
        adjusted = adjust_risk(app["risk_score"], trust)

        refined.append({
            "package": app["package"],
            "trust_level": trust,
            "original_score": app["risk_score"],
            "final_score": adjusted
        })

    return refined
