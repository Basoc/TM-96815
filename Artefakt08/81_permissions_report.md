# Raport Analizy Uprawnień - Artefakt 8.1

**Raport wykonany przez:** Bartłomiej Sokołowski
**Numer studenta:** 96815
**Data:** 2026-06-05

---

## 1. Zawartość RiskyPermission.xml

Zidentyfikowano następujące wpisy krytyczne:

- **Debuggable: true** WYSOKIE RYZYKO - Aplikacja podatna na inżynierię wsteczną
  w czasie rzeczywistym.
- **Permissions:** Wykryto uprawnienia dające dostęp do sieci (`INTERNET`)
  oraz pamięci zewnętrznej (`WRITE_EXTERNAL_STORAGE`), kontaktów (`READ_CONTACTS`),
  kamery (`CAMERA`) i mikrofonu (`RECORD_AUDIO`).

---

## 2. Interpretacja Inżynierska

Z punktu widzenia bezpieczeństwa, najpoważniejszym problemem jest flaga `debuggable`.
Pozwala ona na użycie komendy `adb jdwp` do śledzenia procesów aplikacji
przez osoby niepowołane.

Uprawnienia takie jak `READ_CONTACTS` i `RECORD_AUDIO` w aplikacji demonstracyjnej
(ApiDemos) są nieproporcjonalne do jej funkcjonalności – to klasyczny przypadek
**over-privileged app**.

---

## 3. Akcja Korygująca

Zaleca się wdrożenie skryptu do procesu CI/CD (np. w Jenkins/GitHub Actions),
który będzie automatycznie blokował buildy, jeśli `RiskyPermission.xml` wykaże
flagę `debuggable="true"`.

Dodatkowo należy przeprowadzić przegląd kodu w celu usunięcia zbędnych uprawnień
zgodnie z zasadą **least privilege** (minimalnych uprawnień).