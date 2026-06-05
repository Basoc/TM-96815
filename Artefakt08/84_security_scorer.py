import xml.etree.ElementTree as ET
import json
import os

print(">>> ZADANIE 8.4: OBLICZANIE SECURITY SCORE (ALGORITHM V1) <<<")
print()

score      = 100
deductions = []

xml_path = "RiskyPermission.xml"

if os.path.exists(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        debuggable_el = root.find(".//Debuggable")
        if debuggable_el is not None and debuggable_el.text == "true":
            score -= 30
            deductions.append("[-30] Flaga Debuggable jest AKTYWNA (High Risk)")

        permissions = root.findall(".//Permission")
        perm_count = len(permissions)
        if perm_count > 0:
            deduction = perm_count * 5
            score -= deduction
            deductions.append(
                f"[-{deduction}] Znaleziono {perm_count} ryzykownych uprawnien (LOW, -{5} pkt kazde)"
            )
    except ET.ParseError as e:
        print(f"[WARN] Blad parsowania {xml_path}: {e}")
else:
    print(f"[WARN] Brak pliku {xml_path} – uruchom najpierw 81_manifest_scanner.py")

json_path = "83_vulnerabilities.json"

severity_weights = {
    "CRITICAL": 40,
    "HIGH":     20,
    "MEDIUM":   10,
    "LOW":       5
}

if os.path.exists(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            vulnerabilities = json.load(f)

        for v in vulnerabilities:
            w = severity_weights.get(v["severity"], 0)
            score -= w
            deductions.append(
                f"[-{w}] {v['severity']} luka w {v['library']} ({v['cve_id']}) – {v['description']}"
            )
    except (json.JSONDecodeError, KeyError) as e:
        print(f"[WARN] Blad odczytu {json_path}: {e}")
else:
    print(f"[WARN] Brak pliku {json_path} – uruchom najpierw 83_library_audit.py")


score = max(0, score)

print("Szczegoly odliczen:")
print("-" * 65)
for d in deductions:
    print(f"  {d}")

print()
print("=" * 65)

if score >= 95:
    status = "PASS (Perfect Application)"
elif score >= 50:
    status = "NEEDS FIX (Review Required)"
else:
    status = "REJECTED (Aplikacja niebezpieczna)"

print(f"WYNIK KONCOWY: {score}/100")
print(f"STATUS: {status}")
print("=" * 65)

output_txt = "84_risk_score.txt"
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(f"SECURITY SCORE: {score}/100\n")
    f.write(f"STATUS: {status}\n\n")
    f.write("Szczegoly odliczen:\n")
    for d in deductions:
        f.write(f"  {d}\n")

print(f"\n[SUCCESS] Zapisano wynik do: {output_txt}")
