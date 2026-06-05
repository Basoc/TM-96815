import xml.etree.ElementTree as ET
import os


MANIFEST_PATH = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
OUTPUT_PATH = "RiskyPermission.xml"

dangerous_list = [
    'READ_CONTACTS',
    'WRITE_EXTERNAL_STORAGE',
    'ACCESS_FINE_LOCATION',
    'INTERNET',
    'CAMERA',
    'RECORD_AUDIO',
    'READ_SMS',
    'SEND_SMS',
    'READ_CALL_LOG',
    'ACCESS_COARSE_LOCATION',
    'GET_ACCOUNTS',
    'USE_BIOMETRIC',
    'PROCESS_OUTGOING_CALLS',
]

print(f">>> URUCHAMIANIE AUDYTU: {MANIFEST_PATH} <<<")

if not os.path.exists(MANIFEST_PATH):
    print(f"[BLAD] Nie odnaleziono pliku: {MANIFEST_PATH}")
    print("[INFO] Sprawdz sciezke do AndroidManifest.xml z Artefaktu02")
    exit(1)

tree = ET.parse(MANIFEST_PATH)
root = tree.getroot()

risky_permissions = []
debuggable = False

for app in root.findall('application'):
    dbg = app.get('{http://schemas.android.com/apk/res/android}debuggable')
    if dbg == 'true':
        debuggable = True

for perm in root.findall('uses-permission'):
    name = perm.get('{http://schemas.android.com/apk/res/android}name')
    if name:
        short_name = name.split('.')[-1]
        if short_name in dangerous_list:
            risky_permissions.append(name)

audit = ET.Element(
    'SecurityAudit',
    app="ApiDemos_Security_Check",
    status="ReviewRequired"
)
flags_el = ET.SubElement(audit, 'Flags')
ET.SubElement(flags_el, 'Debuggable').text = str(debuggable).lower()

perms_el = ET.SubElement(audit, 'RiskyPermissions')
for p in risky_permissions:
    ET.SubElement(perms_el, 'Permission').text = p

tree_out = ET.ElementTree(audit)
ET.indent(tree_out, space="  ")
tree_out.write(OUTPUT_PATH, encoding='unicode', xml_declaration=True)

print(f"[SUCCESS] Wygenerowano czytelny raport: {OUTPUT_PATH}")
print(f"[INFO] Znaleziono {len(risky_permissions)} podejrzanych uprawnien.")

if debuggable:
    print("[ALERT] Wykryto aktywna flage DEBUGGABLE! (WYSOKIE RYZYKO)")
else:
    print("[OK] Flaga debuggable nie jest aktywna.")
