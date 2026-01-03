import subprocess

def run_adb(command):
    try:
        result = subprocess.check_output(
            ["adb"] + command,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"ERROR: {e.output}"
