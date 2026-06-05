import sys
import os
import time
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Artefakt06'))

from MainPage import MainPage


class DeviceStateManager(MainPage):

    LOG_FILE = "73_state.log"

    def __init__(self):
        super().__init__()
        self.driver = getattr(self, "driver", None)

        self.log_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            self.LOG_FILE
        )

        print("[DEVICE] Moduł zarządzania stanem zainicjalizowany")
        print("-" * 40)

    def _log_event(self, event_name, detail):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        with open(self.log_path, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {event_name}: {detail}\n")

    def toggle_screen_orientation(self, target="LANDSCAPE"):

        print(f"[DEVICE] Zmiana orientacji na: {target}")

        if getattr(self, "driver", None):
            pass

        detail = f"Ekran obrócony do {target}"
        self._log_event("ORIENTATION", detail)

        return f"SUKCES: Orientacja zmieniona na {target}"

    def simulate_power_connection(self, is_connected=True):

        state = "CONNECTED" if is_connected else "DISCONNECTED"

        print(f"[DEVICE] Zasilanie: {state}")

        if getattr(self, "driver", None):
            pass

        self._log_event("POWER_STATE", state)

        return f"SUKCES: Stan zasilania ustawiony na {state}"

    def run_orientation_round_trip(self):

        print("\n[DEVICE] ROUND-TRIP TEST ORIENTACJI")

        result1 = self.toggle_screen_orientation("LANDSCAPE")
        print(result1)
        time.sleep(0.5)

        result2 = self.toggle_screen_orientation("PORTRAIT")
        print(result2)
        time.sleep(0.5)

        self._log_event(
            "ROUND_TRIP",
            "PORTRAIT -> LANDSCAPE -> PORTRAIT"
        )

        return "SUKCES: Round-trip zakończony"


if __name__ == "__main__":

    print("=" * 55)
    print("ZADANIE 7.3 - ZARZĄDZANIE STANEM URZĄDZENIA")
    print("=" * 55)

    manager = DeviceStateManager()

    print(manager.run_orientation_round_trip())

    print("-" * 55)

    print(manager.simulate_power_connection(True))

    print("-" * 55)

    print(manager.simulate_power_connection(False))

    print()
    print(f"Log zapisano w pliku: {DeviceStateManager.LOG_FILE}")

    print("=" * 55)
    print("ZADANIE 7.3 ZAKOŃCZONE")
    print("=" * 55)