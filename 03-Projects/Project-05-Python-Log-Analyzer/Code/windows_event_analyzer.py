from pathlib import Path

failed_logins = 0
successful_logins = 0
account_lockouts = 0
ip_counts = {}

BASE_DIR = Path(__file__).resolve().parent.parent

log_path = BASE_DIR / "Logs" / "sample_windows_security.log"
report_path = BASE_DIR / "Reports" / "windows_security_report.txt"

with open(log_path, "r", encoding="utf-8") as log_file:
    for line in log_file:
        if "EVENT_ID=4625" in line:
            failed_logins += 1

            for word in line.split():
                if word.startswith("IP="):
                    ip = word.replace("IP=", "")
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1

        elif "EVENT_ID=4624" in line:
            successful_logins += 1

        elif "EVENT_ID=4740" in line:
            account_lockouts += 1

print("=" * 45)
print("WINDOWS SECURITY INCIDENT REPORT")
print("=" * 45)
print(f"Failed Logons: {failed_logins}")
print(f"Successful Logons: {successful_logins}")
print(f"Account Lockouts: {account_lockouts}")
print(f"Unique Attacker IPs: {len(ip_counts)}")

print("\nAttacker Summary")
print("-" * 45)

for ip, count in ip_counts.items():
    print(f"{ip} -> {count} failed attempt(s)")
    if count >= 2:
        print("ALERT: Possible brute-force attack!")

with open(report_path, "w", encoding="utf-8") as report:
    report.write("WINDOWS SECURITY INCIDENT REPORT\n")
    report.write("=" * 45 + "\n")
    report.write(f"Failed Logons: {failed_logins}\n")
    report.write(f"Successful Logons: {successful_logins}\n")
    report.write(f"Account Lockouts: {account_lockouts}\n")
    report.write(f"Unique Attacker IPs: {len(ip_counts)}\n")
    report.write("\nAttacker Summary\n")
    report.write("-" * 45 + "\n")

    for ip, count in ip_counts.items():
        report.write(f"{ip} -> {count} failed attempt(s)\n")
        if count >= 2:
            report.write("ALERT: Possible brute-force attack!\n")

print("\nReport saved successfully!")