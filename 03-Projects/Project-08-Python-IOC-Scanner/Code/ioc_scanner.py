from pathlib import Path

known_iocs = {
    "8.8.8.8": "Google Public DNS",
    "1.1.1.1": "Cloudflare Public DNS",
    "44d88612fea8a8f36de82e1278abb02f": "EICAR test-file MD5 hash"
}

ioc_file = Path(__file__).parent / "sample_iocs.txt"
report_file = Path(__file__).parent.parent / "Reports" / "ioc_report.txt"

indicators = [
    line.strip()
    for line in ioc_file.read_text(encoding="utf-8-sig").splitlines()
    if line.strip()
]

results = []
matches = 0

for indicator in indicators:
    if indicator in known_iocs:
        matches += 1
        results.append(f"[MATCH] {indicator} - {known_iocs[indicator]}")
    else:
        results.append(f"[NO MATCH] {indicator}")

output = [
    "=" * 50,
    "IOC SCANNER REPORT",
    "=" * 50,
    *results,
    "",
    f"Indicators scanned: {len(indicators)}",
    f"Matches found: {matches}"
]

report = "\n".join(output)
print(report)
report_file.write_text(report, encoding="utf-8")

print(f"\nReport saved to: {report_file}")
