# 📱 Mobile Automation & Cloud-Ready Testing Suite

**Prowadzący:** mgr Mariusz Dworniczak 
**Student:** Bartłomiej Sokołowski
**Numer Albumu:** 96815

---

## 🏗️ Architektura Projektu (Marketing & Tech Stack)
Ten projekt to kompletny ekosystem testowy oparty na podejsciu **Cloud-Ready / Headless**. Zamiast polegać na ciężkich emulatorach, skupiamy się na narzędziach CLI, analizie statycznej, konteneryzacji (Docker) oraz automatyzacji procesów (Pipeline). 

**Główne technologie:**
* **Język:** Python 3.10+
* **Automatyzacja UI:** Appium 2.x (Mobile Engine)
* **Infrastruktura:** Docker & Docker Compose
* **Raportowanie:** Allure Framework
* **Analiza:** MobSF (Static Analysis) & ADB CLI

---

## 📅 PRZEBIEG LABORATORIUM (Kamienie Milowe)

### 🔹 BLOK 1: Tooling & Environment (Infrastruktura)
Przygotowanie bazy narzędziowej w modelu kontenerowym.
* **Co zrobiono:** Pobranie i konfiguracja obrazów `appium`, `android-sdk` oraz `mobsf`.
* **Wniosek:** Obrazy Docker eliminują problem "u mnie działa" — każdy obraz zawiera dokładnie tę samą wersję narzędzia, systemu i zależności. Zamiast ręcznie instalować Android SDK, Java i Appium na każdej maszynie, wystarczy jedno polecenie `docker pull`. Środowisko jest przenośne, odizolowane od systemu hosta i gotowe do działania w CI/CD bez żadnych modyfikacji.

### 🔹 BLOK 2: Debugowanie i Analiza Statyczna (MobSF)
Zrozumienie "wnętrza" aplikacji mobilnej przed przystąpieniem do testów.
* **Co zrobiono:** Wykorzystanie MobSF do skanowania plików APK pod kątem podatności i uprawnień.
* **Wniosek:** Analiza statyczna APK daje testerowi wgląd w strukturę aplikacji bez jej uruchamiania — można sprawdzić, jakich uprawnień żąda (np. ACCESS_FINE_LOCATION, READ_CONTACTS), czy nie zawiera zakodowanych na stałe haseł lub kluczy API, jakie biblioteki zewnętrzne są użyte oraz czy kod nie zawiera znanych wzorców podatności. To pozwala wyłapać zagrożenia bezpieczeństwa i nadmiarowe uprawnienia na etapie przed testami dynamicznymi.

### 🔹 BLOK 3-4: Fundamenty Skryptowania (Python for QA)
Budowa logiki testowej w języku Python.
* **Co zrobiono:** Nauka podstawowych struktur danych (listy, słowniki, krotki) oraz funkcji służących do organizacji logiki testowej. Ćwiczono operacje na kolekcjach (iteracja, filtrowanie), obsługę wyjątków (`try/except`) oraz definiowanie funkcji pomocniczych wielokrotnego użytku — takich jak `run_cmd()` zastosowana w finalnym `pipeline.py`. Omawiano też pracę z modułami standardowymi (`os`, `sys`, `subprocess`, `datetime`).

### 🔹 BLOK 5-7: Hybrydowe Testowanie API (Requests & Pytest)
Weryfikacja warstwy backendowej aplikacji mobilnej.
* **Co zrobiono:** Testowanie endpointów REST (JSONPlaceholder), obsługa kodów HTTP i asercja danych JSON.
* **Wniosek:** Testowanie API pozwala wyłapać błędy zanim uruchomimy ciężkie testy UI.

### 🔹 BLOK 8: Appium UI Automation (Deep Dive)
Automatyzacja interakcji z interfejsem użytkownika.
* **Co zrobiono:** Konfiguracja sesji Appium z odpowiednimi `desired_capabilities` (platformName, deviceName, appPackage, appActivity). Do lokalizowania elementów UI używano selektorów `By.ID` (dla unikalnych identyfikatorów zasobów np. `com.example:id/button_login`) oraz `By.XPATH` (dla elementów bez ID, z nawigacją po drzewie widoków). Symulowano akcje takie jak `click()`, `send_keys()` (wpisywanie tekstu) oraz `swipe()` (przewijanie ekranu). Implementowano wzorzec Page Object Model dla czytelności kodu testowego.

### 🔹 BLOK 9: Konteneryzacja Serwera (Docker Compose)
Izolacja silnika Appium od systemu operacyjnego.
* **Co zrobiono:** Stworzenie pliku `docker-compose.yml` zarządzającego serwerem Appium i sterownikami.

### 🔹 BLOK 10: MASTER PIPELINE (Capstone Project) 🏆
Finałowa automatyzacja całego procesu testowego.
* **Co zrobiono:** Stworzenie skryptu `pipeline.py`, który w jednym cyklu:
1. Rezerwuje zasoby i stawia infrastrukturę Docker.
2. Wykonuje testy hybrydowe (API + UI).
3. Generuje profesjonalny raport Allure z metadanymi.
4. Czyści środowisko po zakończonej pracy.

---

## 📊 Raportowanie Wyników (Allure)
Projekt wykorzystuje zaawansowane raportowanie Allure, które pozwala na:
* Śledzenie kroków testowych (`@allure.step`).
* Analizę błędów wraz z załącznikami (zrzuty ekranu, logi JSON).
* Dokumentowanie środowiska wykonawczego w sekcji **Environment**.

**Wyniki ostatniego uruchomienia (2026-06-13 11:29:24):**
| Status | Liczba testów |
|--------|--------------|
| ✅ Passed | 4 |
| ❌ Failed | 2 |
| **Total** | **6** |

> ℹ️ 2 testy oznaczone jako `failed` to testy celowe (`test_intentional_failure`, `test_screenshot_on_fail`) — demonstrują mechanizm zbierania dowodów przez Allure w przypadku błędu (załączniki tekstowe, JSON, symulowane zrzuty ekranu).

**Środowisko wykonawcze zarejestrowane w raporcie:**
```
Pipeline.Status    = SUCCESS
Execution.Time     = 2026-06-13 11:29:24
Execution.Type     = Automated Master Script
Infrastructure     = Docker (Appium Server)
Platform           = win32
Build.Engine       = Python Subprocess
```

---

## 🚀 Jak uruchomić cały proces?
```bash
# Wejdź do folderu finałowego
cd Artefakt10

# Uruchom wszystko jednym poleceniem
python3 pipeline.py

# Po zakończeniu zobacz raport
allure serve allure-results
```
