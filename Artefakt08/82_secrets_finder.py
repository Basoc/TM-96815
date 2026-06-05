import re
import os


strings_path = "../Artefakt02/decompiled_apk/res/values/strings.xml"
output_txt   = "82_secrets_found.txt"

print(f">>> SKANOWANIE ZASOBOW: {strings_path} <<<")

if not os.path.exists(strings_path):
    print(f"[BLAD] Nie odnaleziono pliku zasobow: {strings_path}")
    print("[INFO] Sprawdz sciezke do strings.xml z Artefaktu02")
    exit(1)

with open(strings_path, 'r', encoding='utf-8') as f:
    content = f.read()

patterns = {
    "IP_Address":       r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    "URL_Endpoint":     r'https?://[^\s"\'<>]+',
    "Potential_Secret": r'(?i)\b(key|token|secret|password|auth|api_key|passwd|credential)\b',
    "API_Key_Format":   r'[a-zA-Z0-9_-]{20,}',
}

results = []

for label, pattern in patterns.items():
    matches = re.findall(pattern, content)
    for match in set(matches):
        if len(match) > 3 and not match.endswith('.xml'):
            results.append(f"[{label}] -> {match}")

print(f"[INFO] Analiza zakonczona. Znaleziono {len(results)} potencjalnych punktow wycieku.\n")

for r in results[:15]:
    print(f"  {r}")
if len(results) > 15:
    print(f"  ... i {len(results) - 15} wiecej (wszystkie zapisano w pliku)")

with open(output_txt, 'w', encoding='utf-8') as f:
    f.write(f"# Raport skanowania secrets\n")
    f.write(f"# Plik zrodlowy: {strings_path}\n")
    f.write(f"# Liczba znalezisk: {len(results)}\n\n")
    for r in results:
        f.write(r + "\n")

print(f"\n[SUCCESS] Zapisano {len(results)} wynikow do: {output_txt}")
