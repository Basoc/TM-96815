import json
import os

class BasePage:
    def __init__(self, selectors_file="../Artefakt05/53_selectors.json"):
        with open(selectors_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.selectors = data["selectors"]

        print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(self.selectors)} elementów.")
        print(f"Weryfikacja klucza 'ADD': {self.get_selector('ADD')}")

    def get_selector(self, business_name):
        return self.selectors.get(business_name, None)

    def find_id(self, business_name):
        selector = self.get_selector(business_name)
        if selector:
            print(f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'")
            return selector
        else:
            print(f"BŁĄD: Selektor '{business_name}' nie istnieje w mapie!")
            return None


if __name__ == "__main__":
    page = BasePage()