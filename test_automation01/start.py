from .steps import get_google_title


def start_automation(data, driver):
    text = data.get("text")

    get_google_title(driver, text)