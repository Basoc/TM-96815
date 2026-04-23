import xml.etree.ElementTree as ET
import glob
import json

def check_a11y(path):
    ns = '{http://schemas.android.com/apk/res/android}'
    gaps = []

    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                node_text = elem.get(f'{ns}text')
                node_desc = elem.get(f'{ns}contentDescription')
                node_id = elem.get(f'{ns}id', 'no-id')

                if node_text and not node_desc:
                    gaps.append({
                        "file": file.split('/')[-1],
                        "id": node_id.split('/')[-1],
                        "text": node_text,
                        "issue": "Brak atrybutu contentDescription"
                    })
        except:
            continue

    with open('a11y_report.json', 'w', encoding='utf-8') as f:
        json.dump(gaps, f, indent=4, ensure_ascii=False)

    print(f"[OK] Znaleziono {len(gaps)} elementów z lukami dostępności.")
    print("Zapisano: a11y_report.json")

check_a11y("../Artefakt02/decompiled_apk/res/layout")