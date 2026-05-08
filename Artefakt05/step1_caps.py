import xml.etree.ElementTree as ET
import json
import os

manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"

ns = {'android': 'http://schemas.android.com/apk/res/android'}

tree = ET.parse(manifest_path)
root = tree.getroot()

package = root.attrib.get('package')

main_activity = ""
for activity in root.findall(".//activity", ns):
    intent = activity.find(".//intent-filter", ns)
    if intent is not None:
        action = intent.find(
            ".//action[@{http://schemas.android.com/apk/res/android}name='android.intent.action.MAIN']",
            ns
        )
        if action is not None:
            main_activity = activity.get(
                '{http://schemas.android.com/apk/res/android}name'
            )
            break

capabilities = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": package,
    "appActivity": main_activity,
    "deviceName": "emulator-5554",
    "noReset": True
}

with open("51_caps.json", "w") as f:
    json.dump(capabilities, f, indent=2)

print("=" * 50)
print(f"Sukces! Wykryto: {package} / {main_activity}")
print("=" * 50)
print(json.dumps(capabilities, indent=2))
