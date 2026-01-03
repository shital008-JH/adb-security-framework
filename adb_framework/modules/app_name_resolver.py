from adb_utils import run_adb
import re

def get_app_name(package):
    try:
        output = run_adb(["shell", "dumpsys", "package", package])
        match = re.search(r'application-label:\s*(.+)', output)
        if match:
            return match.group(1).strip()
    except:
        pass
    return package  # fallback if label not found
