from pathlib import Path

known_iocs = {
    "8.8.8.8": "Google Public DNS",
    "1.1.1.1": "Cloudflare Public DNS",
    "44d88612fea8a8f36de82e1278abb02f": "EICAR Test File Hash"
}

ioc_file = Path(__file__).parent / "sample_iocs.txt"

with open(ioc_file, "r") as file:
    indicators = [line.strip() for line in file if line.strip()]

print("=" * 50)
print("IOC SCANNER REPORT")
print("=" * 50)

matches = 0

for indicator in indicators:
    if indicator in known_iocs:
        matches += 1
        print(f"[MATCH] {indicator}")
        print(f"Description: {known_iocs[indicator]}")
    else:
        print(f"[OK] {indicator} - No local match")

print("\nSummary")
print(f"Indicators Scanned: {len(indicators)}")
print(f"Matches Found: {matches}")
    else:
        print(f"[OK] {indicator} - No local match")

print("\nSummary")
print(f"Indicators Scanned: {len(indicators)}")
print(f"Matches Found: {matches}")