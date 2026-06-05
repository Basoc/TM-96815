import json

print(">>> ZADANIE 8.3: ANALIZA LANCUCHA DOSTAW (SCA - Software Composition Analysis) <<<")
print("[INFO] Rozpoczynam skanowanie bibliotek z pliku: requirements.txt...")
print()

cve_database = {
    "com.google.android.gms:10.0.1": {
        "severity":    "HIGH",
        "cve_id":      "CVE-2021-4352",
        "description": "Blad weryfikacji certyfikatu – mozliwe MITM",
        "cvss":        7.5
    },
    "com.squareup.okhttp:2.7.5": {
        "severity":    "MEDIUM",
        "cve_id":      "CVE-2016-2402",
        "description": "Podatnosc na Man-in-the-Middle przez brak pinning",
        "cvss":        5.9
    },
    "org.apache.commons:1.0.0": {
        "severity":    "CRITICAL",
        "cve_id":      "CVE-2015-7501",
        "description": "Zdalne wykonanie kodu (RCE) przez deserializacje Java",
        "cvss":        9.8
    },
    "com.android.support:25.0.0": {
        "severity":    "LOW",
        "cve_id":      "CVE-2019-1234",
        "description": "Wyciek informacji w logach systemowych",
        "cvss":        3.1
    }
}

severity_icons = {
    "CRITICAL": "[CRITICAL]",
    "HIGH":     "[HIGH]   ",
    "MEDIUM":   "[MEDIUM] ",
    "LOW":      "[LOW]    "
}

try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        libraries = [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]
except FileNotFoundError:
    print("[BLAD] Nie znaleziono pliku requirements.txt!")
    exit(1)

found_vulnerabilities = []

for lib in libraries:
    if lib in cve_database:
        vuln = cve_database[lib]
        found_vulnerabilities.append({
            "library":     lib,
            "severity":    vuln["severity"],
            "cve_id":      vuln["cve_id"],
            "description": vuln["description"],
            "cvss":        vuln["cvss"]
        })

print(f"Wynik audytu: Znaleziono {len(found_vulnerabilities)} podatnosci.")
print("-" * 65)

for v in found_vulnerabilities:
    icon = severity_icons.get(v["severity"], v["severity"])
    print(f"{icon} {v['library']}")
    print(f"             Id: {v['cve_id']} | CVSS: {v['cvss']} | Opis: {v['description']}")
    print()

output_json = "83_vulnerabilities.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(found_vulnerabilities, f, indent=2, ensure_ascii=False)

print(f"[SUCCESS] Zapisano raport do: {output_json}")
print(f"[INFO] Format JSON gotowy do importu do systemu Jira/Bugzilla")
