from adb_utils import run_adb
from datetime import datetime
import os

def device_connected():
    output = run_adb(["devices"])
    lines = output.splitlines()
    return any("device" in line and "unauthorized" not in line for line in lines[1:])

def get_device_info():
    info = {}

    info["Model"] = run_adb(["shell", "getprop", "ro.product.model"])
    info["Manufacturer"] = run_adb(["shell", "getprop", "ro.product.manufacturer"])
    info["Android Version"] = run_adb(["shell", "getprop", "ro.build.version.release"])
    info["SDK Level"] = run_adb(["shell", "getprop", "ro.build.version.sdk"])
    info["Build ID"] = run_adb(["shell", "getprop", "ro.build.id"])
    info["SELinux Mode"] = run_adb(["shell", "getenforce"])

    info["CPU Info"] = run_adb(
        ["shell", "cat", "/proc/cpuinfo"]
    ).split("\n")[0]

    info["Battery"] = run_adb(["shell", "dumpsys", "battery"])

    return info

def save_report(info):
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/device_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("ANDROID DEVICE INTELLIGENCE REPORT\n")
        f.write("=" * 45 + "\n\n")

        for key, value in info.items():
            f.write(f"{key}:\n{value}\n")
            f.write("-" * 45 + "\n")

    return filename
