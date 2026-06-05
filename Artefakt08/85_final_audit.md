# RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS

**Data:** 2026-06-05
**Audytor:** Bartłomiej Sokołowski | Nr studenta: 96815
**Projekt:** ApiDemos - Statyczna Analiza Bezpieczeństwa (MobSF)

---

## 1. OCENA KOŃCOWA (SECURITY SCORE)

**WYNIK:** 0/100
**STATUS:** REJECTED (Aplikacja niebezpieczna)

> Wynik pochodzi z pliku `84_risk_score.txt` wygenerowanego przez skrypt `84_security_scorer.py`.

---

## 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)

**Problem:**
Aktywna flaga `debuggable="true"` w `AndroidManifest.xml`.
Wykryto 5 ryzykownych uprawnień: `INTERNET`, `READ_CONTACTS`,
`WRITE_EXTERNAL_STORAGE`, `RECORD_AUDIO`, `CAMERA`.

**Wpływ:**
Możliwość inżynierii wstecznej w czasie rzeczywistym przez `adb jdwp`.
Aplikacja ma dostęp do kontaktów, plików i mikrofonu bez uzasadnienia biznesowego
(klasyczny przypadek **over-privileged app**).

---

### B. Wycieki Danych (Zadanie 8.2)

**Problem:**
W pliku `strings.xml` wykryto twardo zakodowane adresy URL, słowa kluczowe
sugerujące obecność haseł (`password`, `auth`) oraz długie ciągi alfanumeryczne
pasujące do wzorca klucza API.

**Wpływ:**
Potencjalny wyciek endpointów API i poświadczeń do napastnika po dekompilacji APK
(proces dekompilacji zajmuje napastnikowi dosłownie kilka sekund).

---

### C. Biblioteki Zewnętrzne (Zadanie 8.3)

**Problem:**
Zidentyfikowano 4 podatne biblioteki:
- `org.apache.commons:1.0.0` → **CRITICAL** – RCE (CVE-2015-7501, CVSS: 9.8)
- `com.google.android.gms:10.0.1` → **HIGH** – błąd weryfikacji certyfikatu (CVE-2021-4352)
- `com.squareup.okhttp:2.7.5` → **MEDIUM** – Man-in-the-Middle (CVE-2016-2402)
- `com.android.support:25.0.0` → **LOW** – wyciek w logach (CVE-2019-1234)

**Wpływ:**
Zdalne wykonanie kodu (RCE) przez napastnika bez interakcji użytkownika.
Podatność na przechwycenie komunikacji sieciowej (MITM).

---

## 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)

1. **[PRIORYTET 1 – KRYTYCZNY]:** Natychmiastowa aktualizacja `org.apache.commons`
   do wersji bez CVE-2015-7501. Podatność RCE jest nieakceptowalna w produkcji.

2. **[PRIORYTET 1 – WYSOKI]:** Ustawienie `debuggable="false"` przed każdym
   buildem produkcyjnym. Dodać automatyczny check do pipeline'u CI/CD
   (Jenkins / GitHub Actions).

3. **[PRIORYTET 2 – ŚREDNI]:** Przeniesienie kluczy API i URL-i do zmiennych
   środowiskowych lub Android Keystore - usunięcie wszelkich sekretów z `strings.xml`.

---

## WNIOSKI KOŃCOWE

Aplikacja ApiDemos **nie może zostać wydana na rynek** w obecnym stanie.

Łączny wynik bezpieczeństwa wynosi **0/100**, co oznacza automatyczne odrzucenie
(`REJECTED`). Krytyczna podatność RCE w łańcuchu dostaw w połączeniu z aktywnym
trybem debug stanowi bezpośrednie zagrożenie dla użytkowników końcowych.

**Decyzja Go/No-Go:** **NO-GO**

Zaleca się wstrzymanie procesu release i przeprowadzenie pełnego cyklu naprawczego
przed kolejnym audytem bezpieczeństwa.