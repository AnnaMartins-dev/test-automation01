import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_google_title(driver, text):
    try:
        print("Navigating to website...")
        driver.get("https://www.google.com")

        if "Google" == driver.title:
            print(f"Success! Page title is: {driver.title}")
        else:
            raise RuntimeError("Titulo diferente")

        search_bar = driver.find_element(By.XPATH, "//textarea[@name='q']")

        search_bar.clear()
        search_bar.send_keys(text)
        time.sleep(5)
        search_bar.send_keys(Keys.ENTER)

        time.sleep(10)

    finally:
        driver.quit()

