import json
import os

caps_path = "51_caps.json"
selectors_path = "53_selectors.json"

print(">>> ZADANIE 5.4: INTEGRACJA ARTEFAKTÓW (STABLE BUILD) <<<")

with open(caps_path, 'r') as f:
    caps_data = json.load(f)

with open(selectors_path, 'r') as f:
    ui_map = json.load(f)

app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")
ui_count = len(ui_map.get("selectors", {}))

if not app_pkg or not app_act:
    status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
    color = "\033[91m"
else:
    status_msg = "READY TO CONNECT"
    color = "\033[92m"

reset = "\033[0m"

report_lines = [
    "=== ARTEFAKT 5.4: SESSION READINESS REPORT ===",
    f"Target App      : {app_pkg}",
    f"Main Activity   : {app_act}",
    f"Device          : {dev_name}",
    f"UI Elements     : {ui_count} loaded",
    f"Status          : {status_msg}",
]

for line in report_lines:
    print(line)

print(f"\n{color}Status : {status_msg}{reset}")

with open("54_session.log", "w") as f:
    f.write("\n".join(report_lines))

print("\n[OK] Artefakt zapisany jako: 54_session.log")