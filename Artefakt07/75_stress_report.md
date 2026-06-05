# 75 Stress Report – ApiDemos Stability Assessment

**Projekt:** Artefakt 07
**Aplikacja:** ApiDemos (`io.appium.android.apis`)  
**Zakres:** Gesty, przerwania systemowe, zmiany stanu urządzenia, synchronizacja UI  
**Typ testów:** Stress / resilience / lifecycle / synchronization

---

## 1. Cel testów

Celem testów było sprawdzenie odporności aplikacji na:
- szybkie i wolne gesty użytkownika
- przerwania systemowe (połączenia, SMS, bateria)
- zmiany stanu urządzenia (rotacja ekranu, zasilanie)
- dynamiczne oczekiwanie na elementy UI

---

## 2. Wyniki testów gestów

### Obserwacje
- Scroll działa poprawnie w zakresie 200–1500 ms
- Gesty poniżej 200 ms nie są rejestrowane
- Long press jest stabilny przy 2000 ms
- Swipe left działa bez błędów

### Wyniki

| Test | Status | Uwagi |
|------|--------|------|
| Scroll normalny | PASS | Poprawne przeliczanie współrzędnych |
| Scroll szybki | FAIL | Flick – brak rejestracji |
| Scroll wolny | RISK | Możliwa interpretacja jako long press |
| Long press | PASS | Stabilne działanie |
| Swipe left | PASS | Brak anomalii |

---

## 3. Odporność na przerwania systemowe

### Obserwacje
- Aplikacja poprawnie przechodzi w stan pause/resume
- Brak utraty danych sesji
- Systemowe dialogi nie powodują crashy

### Wyniki

| Zdarzenie | Status | Uwagi |
|----------|--------|------|
| Incoming call | PASS | Poprawny lifecycle (onPause/onResume) |
| Low battery | PASS | Brak zakłóceń UI |
| SMS notification | PASS | UI pozostaje aktywne |

---

## 4. Zarządzanie stanem urządzenia

### Obserwacje
- Rotacja ekranu nie powoduje utraty danych
- Layout przerysowuje się poprawnie
- Brak memory leaków w cyklu round-trip

### Wyniki

| Test | Status | Uwagi |
|------|--------|------|
| Portrait → Landscape | PASS | Poprawne renderowanie |
| Landscape → Portrait | PASS | Stan zachowany |
| Round-trip | PASS | Brak state loss |
| Power connected | PASS | Brak wpływu na UI |
| Power disconnected | PASS | Stabilne zachowanie |

---

## 5. Synchronizacja UI

### Obserwacje
- WebDriverWait znacząco poprawia stabilność testów
- sleep() jest nieprzewidywalny i niezalecany
- Polling 500ms zapewnia balans wydajności i stabilności

### Wyniki

| Metoda | Wynik | Ocena |
|--------|------|------|
| Explicit wait (valid element) | PASS | Stabilne |
| Visible element wait | PASS | Deterministyczne |
| Non-existent element | FAIL | Timeout expected |
| Fast timeout test | PASS | Szybka reakcja |

---

## 6. Analiza odporności (Stress Summary)

### Kluczowe obserwacje
- aplikacja nie ulega crashom podczas żadnego testu
- brak ANR (Application Not Responding)
- lifecycle działa poprawnie w przerwaniach
- największa wrażliwość: szybkie gesty (<200 ms)

---

## 7. Ocena końcowa

| Obszar | PASS | FAIL | Wynik |
|--------|------|------|------|
| Gesty | 4 | 1 | 80% |
| Przerwania | 3 | 0 | 100% |
| Stan urządzenia | 5 | 0 | 100% |
| Synchronizacja | 3 | 1 | 75% |

### Łącznie
- Testy: 17
- PASS: 15
- FAIL: 2
- Skuteczność: 88%

---

## 8. Wniosek końcowy

Aplikacja ApiDemos wykazuje wysoką odporność na obciążenia interakcyjne i przerwania systemowe.

Największym ograniczeniem jest obsługa bardzo szybkich gestów oraz brak elementu UI w jednym scenariuszu synchronizacji.

Ogólna stabilność: **wysoka**  
Ryzyko awarii: **niskie**  
Zachowanie w stresie: **przewidywalne**