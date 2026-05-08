import xml.etree.ElementTree as ET
import os

manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"

ns = {'android': 'http://schemas.android.com/apk/res/android'}

tree = ET.parse(manifest_path)
root = tree.getroot()

package = root.attrib.get('package')

permissions = [
    elem.attrib.get('{http://schemas.android.com/apk/res/android}name')
    for elem in root.findall('uses-permission')
]

activities = [
    elem.attrib.get('{http://schemas.android.com/apk/res/android}name')
    for elem in root.findall('.//activity')
]

lines = []
lines.append(">>> ZADANIE 5.2: ANALIZA MANIFESTU (POŁĄCZENIE Z ARTEFAKTEM 02) <<<")
lines.append("=== ARTEFAKT 5.2: RAPORT ANALIZY SYSTEMOWEJ ===")
lines.append(f"Pakiet główny: {package}")
lines.append(f"Liczba Activity: {len(activities)}")
lines.append("")
lines.append("Kluczowe Uprawnienia (Co aplikacja chce robić?):")
for perm in permissions:
    if perm:
        lines.append(f"  - {perm}")
lines.append("")
lines.append("[OK] Sukces! Artefakt zapisany jako: 52_inspection.log")

for line in lines:
    print(line)

with open("52_inspection.log", "w") as f:
    f.write("\n".join(lines))