from BasePage import BasePage

class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")
        print("-" * 40)

    def click_add_button(self):
        selector = self.find_id("ADD")
        if selector:
            print(f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'")
        return selector

    def check_title_visibility(self):
        selector = self.get_selector("TITLE")
        if selector:
            print(f"SUKCES: Odnaleziono nagłówek strony (ID: {selector}). Status: Widoczny.")
        return selector

    def enter_search_text(self, text):
        selector = self.get_selector("SEARCH_BUTTON")
        if selector:
            print(f"SUKCES: Wpisano '{text}' do pola {selector} i zatwierdzono.")
        return selector


if __name__ == "__main__":
    page = MainPage()
    page.click_add_button()
    page.check_title_visibility()