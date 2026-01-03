from modules.device_info import (
    device_connected,
    get_device_info,
    save_report
)

def main():
    print("\n🔍 Initializing Device Intelligence Engine...\n")

    if not device_connected():
        print("❌ No authorized Android device detected.")
        return

    print("✅ Device connected successfully\n")

    info = get_device_info()

    print("📱 DEVICE INTELLIGENCE SUMMARY")
    print("-" * 45)

    for key, value in info.items():
        print(f"{key}:")
        print(value)
        print("-" * 45)

    report_path = save_report(info)
    print(f"\n📁 Report saved to: {report_path}")

if __name__ == "__main__":
    main()
