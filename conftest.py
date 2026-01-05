import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.urls import BASE_URL


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--no-first-run')
    options.add_argument('--disable-popup-blocking')

    prefs = {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
    }
    options.add_experimental_option('prefs', prefs)

    # На новых Chrome это часто решает именно окно про "утечку пароля"
    options.add_argument('--disable-features=PasswordLeakDetection')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(BASE_URL)

    yield driver

    driver.quit()
