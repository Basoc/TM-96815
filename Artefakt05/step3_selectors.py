import xml.etree.ElementTree as ET
import json
import os

layout_dir = "../Artefakt02/decompiled_apk/res/layout/"

ui_map = {
    "selectors": {}
}

for file_name in os.listdir(layout_dir):
    if file_name.endswith(".xml"):
        try:
            tree = ET.parse(os.path.join(layout_dir, file_name))
            root = tree.getroot()

            for element in root.iter():
                res_id = element.attrib.get(
                    '{http://schemas.android.com/apk/res/android}id'
                )
                if res_id:
                    clean_id = res_id.split('/')[-1]
                    business_name = clean_id.upper()
                    ui_map["selectors"][business_name] = clean_id
        except:
            continue

count = len(ui_map["selectors"])

print(">>> ZADANIE 5.3: BUDOWA MAPY SELEKTORÓW (UI MAPPING) <<<")
print(f"[OK] Zmapowano {count} unikalnych elementów UI.")
print("Artefakt zapisany: 53_selectors.json")

with open("53_selectors.json", "w") as f:
    json.dump(ui_map, f, indent=2)