from adb_utils import run_adb

def get_setting(namespace, key):
    return run_adb(["shell", "settings", "get", namespace, key]).strip()

def is_usb_debugging_enabled():
    return get_setting("global", "adb_enabled") == "1"

def is_developer_options_enabled():
    return get_setting("global", "development_settings_enabled") == "1"

def get_selinux_status():
    return run_adb(["shell", "getenforce"]).strip()

def is_device_encrypted():
    output = run_adb(["shell", "getprop", "ro.crypto.state"])
    return "encrypted" in output.lower()

def get_lock_screen_status():
    output = run_adb(["shell", "dumpsys", "trust"])
    return "unlocked" not in output.lower()

def run_security_audit():
    findings = {}

    findings["USB Debugging"] = is_usb_debugging_enabled()
    findings["Developer Options"] = is_developer_options_enabled()
    findings["SELinux"] = get_selinux_status()
    findings["Encrypted Storage"] = is_device_encrypted()
    findings["Screen Lock Enabled"] = get_lock_screen_status()

    return findings

def calculate_risk_score(findings):
    score = 0

    if findings["USB Debugging"]:
        score += 30
    if findings["Developer Options"]:
        score += 20
    if findings["SELinux"] != "Enforcing":
        score += 30
    if not findings["Encrypted Storage"]:
        score += 40
    if not findings["Screen Lock Enabled"]:
        score += 40

    return min(score, 100)
