from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

log_file = BASE_DIR / "Captures" / "sample_network.log"
report_file = BASE_DIR / "Reports" / "network_report.txt"

protocol_counts = {}
source_counts = {}

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()

        src = parts[1].replace("SRC=", "")
        protocol = parts[3].replace("PROTOCOL=", "")

        protocol_counts[protocol] = protocol_counts.get(protocol, 0) + 1
        source_counts[src] = source_counts.get(src, 0) + 1

print("=" * 50)
print("NETWORK TRAFFIC SUMMARY")
print("=" * 50)

print("\nProtocols")
for protocol, count in protocol_counts.items():
    print(f"{protocol}: {count}")

print("\nSource IP Activity")
for ip, count in source_counts.items():
    print(f"{ip}: {count}")

with open(report_file, "w", encoding="utf-8") as report:
    report.write("NETWORK TRAFFIC SUMMARY\n")
    report.write("=" * 50 + "\n\n")

    report.write("Protocols\n")
    for protocol, count in protocol_counts.items():
        report.write(f"{protocol}: {count}\n")

    report.write("\nSource IP Activity\n")
    for ip, count in source_counts.items():
        report.write(f"{ip}: {count}\n")

print("\nReport created successfully!")