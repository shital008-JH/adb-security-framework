from adb_utils import run_adb

DANGEROUS_PERMISSIONS = [
    "android.permission.READ_CONTACTS",
    "android.permission.READ_SMS",
    "android.permission.SEND_SMS",
    "android.permission.RECORD_AUDIO",
    "android.permission.CAMERA",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.READ_CALL_LOG",
    "android.permission.WRITE_CALL_LOG",
    "android.permission.READ_EXTERNAL_STORAGE",
    "android.permission.WRITE_EXTERNAL_STORAGE"
]

def list_packages():
    output = run_adb(["shell", "pm", "list", "packages"])
    return [line.replace("package:", "") for line in output.splitlines()]

def get_granted_permissions(package):
    output = run_adb(["shell", "dumpsys", "package", package])
    granted = []

    for line in output.splitlines():
        if "granted=true" in line.lower():
            for perm in DANGEROUS_PERMISSIONS:
                if perm in line:
                    granted.append(perm)

    return list(set(granted))

def analyze_permission_risk():
    results = []
    packages = list_packages()

    for pkg in packages:
        perms = get_granted_permissions(pkg)
        if perms:
            results.append({
                "package": pkg,
                "dangerous_permissions": perms,
                "risk_score": len(perms) * 10
            })

    return results
