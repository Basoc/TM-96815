import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime

print(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")
print("")
print("---- FEEDBACK DLA TWÓRCÓW APLIKACJI ----")

with open("51_caps.json", "r") as f:
    caps_data = json.load(f)

with open("53_selectors.json", "r") as f:
    ui_map = json.load(f)

current_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
feedback_report = []

if current_pkg == "io.appium.android.apis":
    feedback_report.append({
        "feature": "Identyfikacja Aplikacji",
        "status": "ZGODNY",
        "message": f"Pakiet {current_pkg} poprawnie zmapowany."
    })
    pkg_status = "pass"
else:
    feedback_report.append({
        "feature": "Identyfikacja Aplikacji",
        "status": "DO POPRAWY",
        "message": f"Niezgodność pakietu. Wykryto {current_pkg}, sprawdź konfigurację manifestu."
    })
    pkg_status = "failure"

target_element = "ACCESSIBILITY"
available_keys = list(ui_map["selectors"].keys())

if target_element in ui_map["selectors"]:
    feedback_report.append({
        "feature": "Dostępność UI",
        "status": "ZGODNY",
        "message": f"Element {target_element} jest dostępny w layoutach."
    })
    ui_status = "pass"
else:
    feedback_report.append({
        "feature": "Dostępność UI",
        "status": "INFORMACJA",
        "message": (
            f"Nie odnaleziono ID '{target_element}'. "
            f"Sugestia: Zweryfikuj czy element nie zmienił nazwy "
            f"na jedną z dostępnych: {available_keys[:3]}."
        )
    })
    ui_status = "failure"

for item in feedback_report:
    print(f"[{item['status']}] {item['feature']}: {item['message']}")

testsuites = ET.Element("testsuites")
testsuite = ET.SubElement(testsuites, "testsuite",
    name="Artefakt05_ConsistencyTest",
    tests="2",
    timestamp=datetime.datetime.now().isoformat()
)

tc1 = ET.SubElement(testsuite, "testcase",
    name="test_package_identification",
    classname="ConsistencyTest"
)
if pkg_status == "failure":
    fail1 = ET.SubElement(tc1, "failure", message=feedback_report[0]["message"])
    fail1.text = feedback_report[0]["message"]

tc2 = ET.SubElement(testsuite, "testcase",
    name="test_ui_element_accessibility",
    classname="ConsistencyTest"
)
if ui_status == "failure":
    fail2 = ET.SubElement(tc2, "failure", message=feedback_report[1]["message"])
    fail2.text = feedback_report[1]["message"]

xml_str = minidom.parseString(
    ET.tostring(testsuites, encoding='unicode')
).toprettyxml(indent="  ")

with open("55_result.xml", "w") as f:
    f.write(xml_str)

print("")
print("[INFO] Blok 5 zakończony. Raport opisowy gotowy: 55_result.xml")