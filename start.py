from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from automations.default import get_default_options
from steps import get_google_title


def start_webdriver():
    chrome_options = Options()

    chrome_options = get_default_options(chrome_options)

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=chrome_options
    )

    return driver


def start_automation(data):
    text = data.get("text")

    driver = start_webdriver()
    get_google_title(driver, text)