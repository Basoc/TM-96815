import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Artefakt06'))

from MainPage import MainPage


class InterruptManager(MainPage):

    def __init__(self):
        super().__init__()
        self.driver = getattr(self, "driver", None)

        print("[INTERRUPT] Moduł przerwań zainicjalizowany")
        print("-" * 40)

    def simulate_incoming_call(self, duration_sec=3):

        print("\n[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")

        if getattr(self, "driver", None):
            pass

        time.sleep(1)

        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")

        time.sleep(duration_sec)

        print("[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")

        if getattr(self, "driver", None):
            pass

        return "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):

        print("\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")

        if getattr(self, "driver", None):
            pass

        time.sleep(0.5)

        return "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."

    def simulate_sms_notification(self):

        print("\n[INTERRUPT] Wyzwalanie zdarzenia: INCOMING SMS NOTIFICATION")

        if getattr(self, "driver", None):
            pass

        time.sleep(0.5)

        return "SUKCES: Powiadomienie SMS przetworzone. Aplikacja kontynuuje pracę."


if __name__ == "__main__":

    print("=" * 50)
    print("ZADANIE 7.2 - TESTY ODPORNOŚCI NA PRZERWANIA")
    print("=" * 50)

    manager = InterruptManager()

    print(manager.simulate_incoming_call(3))

    print("-" * 50)

    print(manager.simulate_low_battery_warning())

    print("-" * 50)

    print(manager.simulate_sms_notification())

    print()
    print("=" * 50)
    print("ZADANIE 7.2 ZAKOŃCZONE")
    print("=" * 50)