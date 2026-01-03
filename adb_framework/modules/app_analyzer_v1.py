from adb_utils import run_adb

def list_packages():
    output = run_adb(["shell", "pm", "list", "packages"])
    return [line.replace("package:", "") for line in output.splitlines()]

def get_basic_app_info(package):
    info = {}

    info["package"] = package
    info["apk_path"] = run_adb(
        ["shell", "pm", "path", package]
    ).strip()

    info["installer"] = run_adb(
        ["shell", "pm", "get-install-source", package]
    ).strip()

    return info

def get_permissions_summary(package):
    output = run_adb(["shell", "dumpsys", "package", package])
    permissions = []

    for line in output.splitlines():
        if "android.permission." in line:
            permissions.append(line.strip())

    return permissions[:8]  # safe limit
