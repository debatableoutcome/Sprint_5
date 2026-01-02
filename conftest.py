import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
