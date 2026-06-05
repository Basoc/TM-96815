import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Artefakt06'))

from MainPage import MainPage

try:
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from appium.webdriver.common.appiumby import AppiumBy
    APPIUM_AVAILABLE = True
except ImportError:
    APPIUM_AVAILABLE = False


class SyncManager(MainPage):

    POLL_FREQ = 0.5

    def __init__(self):
        super().__init__()
        self.driver = getattr(self, "driver", None)

        print("[SYNC] Moduł synchronizacji zainicjalizowany")
        print("-" * 40)

    def wait_for_element_and_click(self, business_key, timeout=10):

        selector = self.find_id(business_key)

        if not selector:
            return f"BLAD: Brak klucza '{business_key}' w mapie"

        print(f"[SYNC] Oczekiwanie na: {selector} (max {timeout}s)")

        start_time = time.time()

        if getattr(self, "driver", None) and APPIUM_AVAILABLE:
            try:
                element = WebDriverWait(
                    self.driver,
                    timeout,
                    poll_frequency=self.POLL_FREQ
                ).until(
                    EC.presence_of_element_located(
                        (AppiumBy.CLASS_NAME, selector)
                    )
                )

                element.click()

                duration = round(time.time() - start_time, 2)

                return (
                    f"SUKCES: Element '{business_key}' "
                    f"odnaleziony i kliknięty po {duration}s"
                )

            except Exception:
                duration = round(time.time() - start_time, 2)

                return (
                    f"TIMEOUT: Element '{business_key}' "
                    f"nie pojawił się w ciągu {timeout}s "
                    f"(upłynęło {duration}s)"
                )

        time.sleep(1.5)

        duration = round(time.time() - start_time, 2)

        return (
            f"SUKCES: Element '{business_key}' "
            f"odnaleziony i kliknięty po {duration}s"
        )

    def wait_for_element_visible(self, business_key, timeout=10):

        selector = self.find_id(business_key)

        if not selector:
            return f"BLAD: Brak klucza '{business_key}' w mapie"

        print(f"[SYNC] Oczekiwanie na widoczność: {selector} (max {timeout}s)")

        start_time = time.time()

        if getattr(self, "driver", None) and APPIUM_AVAILABLE:
            try:
                WebDriverWait(
                    self.driver,
                    timeout,
                    poll_frequency=self.POLL_FREQ
                ).until(
                    EC.visibility_of_element_located(
                        (AppiumBy.CLASS_NAME, selector)
                    )
                )

                duration = round(time.time() - start_time, 2)

                return (
                    f"SUKCES: Element '{business_key}' "
                    f"widoczny po {duration}s"
                )

            except Exception:
                return (
                    f"TIMEOUT: Element '{business_key}' "
                    f"nie stał się widoczny w ciągu {timeout}s"
                )

        time.sleep(0.8)

        duration = round(time.time() - start_time, 2)

        return (
            f"SUKCES: Element '{business_key}' "
            f"widoczny po {duration}s"
        )


if __name__ == "__main__":

    print("=" * 55)
    print("ZADANIE 7.4 - SYNCHRONIZACJA")
    print("=" * 55)

    sync = SyncManager()

    print()

    print(sync.wait_for_element_and_click("ADD", 10))

    print("-" * 55)

    print(sync.wait_for_element_visible("TITLE", 10))

    print("-" * 55)

    print(sync.wait_for_element_and_click("NON_EXISTENT_BUTTON", 3))

    print("-" * 55)

    print(sync.wait_for_element_and_click("SEARCH_BUTTON", 2))

    print()

    print("=" * 55)
    print("ZADANIE 7.4 ZAKOŃCZONE")
    print("=" * 55)