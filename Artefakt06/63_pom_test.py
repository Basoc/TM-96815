from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: TEST SCENARIUSZA W ARCHITEKTURZE POM <<<")
    print()

    page = MainPage()

    print("---- PRZEBIEG SCENARIUSZA TESTOWEGO ----")

    result1 = page.check_title_visibility()
    if result1:
        print(f"KROK 1: SUKCES: Odnaleziono nagłówek strony (ID: {result1}). Status: Widoczny.")

    result2 = page.click_add_button()
    if result2:
        print(f"KROK 2: SUKCES: Wykonano kliknięcie w element UI o ID: '{result2}'")

    result3 = page.enter_search_text("Automatyzacja Mobilna")
    if result3:
        print(f"KROK 3: SUKCES: Wpisano 'Automatyzacja Mobilna' do pola {result3} i zatwierdzono.")

    print()

    log_content = (
        f"Test Execution Log:\n"
        f"KROK 1: Sprawdzono widoczność tytułu - ID: {result1}\n"
        f"KROK 2: Kliknięto przycisk ADD - ID: {result2}\n"
        f"KROK 3: Wpisano tekst w pole wyszukiwania - ID: {result3}\n"
    )
    with open("64_pom_audit.log", "w", encoding="utf-8") as f:
        f.write(log_content)

    print("[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log")

if __name__ == "__main__":
    run_pom_test()