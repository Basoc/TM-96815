import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Artefakt06'))

from MainPage import MainPage


class GestureAutomator(MainPage):

    def __init__(self):
        super().__init__()
        print("[GESTURE] Moduł gestów zainicjalizowany")
        print("-" * 40)

    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):

        print(f"[GESTURE] Scroll {start_y} -> {end_y} ({duration_ms}ms)")

        if duration_ms < 200:
            return "BLAD: Gest za szybki (flick - brak reakcji UI)"

        scroll_percent = int((start_y - end_y) * 100)

        if getattr(self, "driver", None):
            pass

        return f"SUKCES: Przewinięto {scroll_percent}% ekranu"

    def long_press_element(self, element_key, duration_ms=2000):

        selector = self.find_id(element_key)

        if not selector:
            return f"BLAD: Selektor '{element_key}' nie istnieje w MainPage"

        if duration_ms < 500:
            return "BLAD: Long press za krótki (min 500ms)"

        if getattr(self, "driver", None):
            pass

        return f"SUKCES: LONG PRESS -> {selector} ({duration_ms}ms)"

    def swipe_left(self, start_x=0.8, end_x=0.2, y=0.5, duration_ms=600):

        print(f"[GESTURE] Swipe LEFT {start_x} -> {end_x} (Y={y})")

        if duration_ms < 200:
            return "BLAD: Gest za szybki"

        swipe_percent = int((start_x - end_x) * 100)

        if getattr(self, "driver", None):
            pass

        return f"SUKCES: Swipe LEFT {swipe_percent}% szerokości ekranu"


if __name__ == "__main__":

    print("=" * 50)
    print("ZADANIE 7.1 - GESTY")
    print("=" * 50)

    automator = GestureAutomator()

    print()

    print(automator.scroll_down_logic(0.8, 0.2, 800))
    time.sleep(0.2)

    print(automator.scroll_down_logic(0.9, 0.1, 100))
    time.sleep(0.2)

    print(automator.scroll_down_logic(0.7, 0.3, 1500))
    time.sleep(0.2)

    print()

    print(automator.long_press_element("ADD", 2000))
    time.sleep(0.2)

    print(automator.long_press_element("TITLE", 2000))
    time.sleep(0.2)

    print(automator.long_press_element("SEARCH_BUTTON", 2000))
    time.sleep(0.2)

    print()

    print(automator.swipe_left(0.85, 0.15, 0.5, 600))
    time.sleep(0.2)

    print()

    print("=" * 50)
    print("ZADANIE 7.1 ZAKOŃCZONE")
    print("=" * 50)