# ===================================================
# Project: Python Security Log Analyzer
# Author: Jose Alvarez
# Version: 1.0
#
# Description:
# Reads Linux SSH authentication logs,
# detects failed login attempts,
# identifies attacker IP addresses,
# and generates a security report.
# ===================================================

ip_counts = {}
total_failed_logins = 0
successful_logins = 0

log_path = (
    "03-Projects/Project-05-Python-Log-Analyzer/"
    "Project-05-Python-Log-Analyzer/Logs/sample_auth.log"
)

report_path = (
    "03-Projects/Project-05-Python-Log-Analyzer/"
    "Project-05-Python-Log-Analyzer/Reports/security_report.txt"
)

with open(log_path, "r", encoding="utf-8") as log_file:
    for line in log_file:
        if "Failed password" in line:
            total_failed_logins += 1

            words = line.split()
            attacker_ip = words[-1]

            if attacker_ip in ip_counts:
                ip_counts[attacker_ip] += 1
            else:
                ip_counts[attacker_ip] = 1

        if "Accepted password" in line:
            successful_logins += 1

print("=" * 40)
print("     SECURITY INCIDENT REPORT")
print("=" * 40)
print(f"Total Failed Logins : {total_failed_logins}")
print(f"Successful Logins   : {successful_logins}")
print(f"Unique Attacker IPs : {len(ip_counts)}")

print("\nAttacker Summary")
print("-" * 40)

for ip, count in ip_counts.items():
    print(f"{ip} -> {count} failed login(s)")

    if count >= 2:
        print("   ALERT: Possible brute-force attack!")

print("\nAnalysis Complete")
print("=" * 40)

with open(report_path, "w", encoding="utf-8") as report:
    report.write("SECURITY INCIDENT REPORT\n")
    report.write("========================\n\n")
    report.write(f"Total Failed Logins: {total_failed_logins}\n")
    report.write(f"Successful Logins: {successful_logins}\n")
    report.write(f"Unique Attacker IPs: {len(ip_counts)}\n\n")
    report.write("Attacker Summary\n")
    report.write("------------------------\n")

    for ip, count in ip_counts.items():
        report.write(f"{ip} -> {count} failed login(s)\n")

        if count >= 2:
            report.write("ALERT: Possible brute-force attack!\n")

print("\nSecurity report saved successfully!")