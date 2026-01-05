import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.urls import BASE_URL
from mock_data import EXISTING_ACC


class TestLogin:

    def test_login_success(self, driver):
        email = EXISTING_ACC['email']
        password = EXISTING_ACC['password']

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_ENTER).click()

        wait = WebDriverWait(driver, 10)

        assert wait.until(EC.url_contains(BASE_URL))
        assert wait.until(EC.visibility_of_element_located(locators.USER_AVATAR)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(locators.USER_NAME)).is_displayed()
