

import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.urls import LOGIN_URL
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

        avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
        user_name = wait.until(EC.presence_of_element_located(locators.USER_NAME))



        wait.until(EC.url_contains(LOGIN_URL))
        cur_url = driver.current_url

        assert avatar
        assert cur_url == LOGIN_URL
        assert 'User' in user_name.text
