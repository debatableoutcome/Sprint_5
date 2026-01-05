
import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mock_data import EXISTING_ACC
from config.urls import BASE_URL

class TestLogout:

    def test_logout_success(self, driver):
        email = EXISTING_ACC['email']
        password = EXISTING_ACC['password']

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_ENTER).click()

        wait = WebDriverWait(driver, 10)


        assert wait.until(EC.visibility_of_element_located(locators.USER_AVATAR))
        assert wait.until(EC.visibility_of_element_located(locators.USER_NAME))

        driver.find_element(*locators.BTN_LOGOUT).click()


        assert wait.until(EC.invisibility_of_element_located(locators.USER_AVATAR))
        assert wait.until(EC.invisibility_of_element_located(locators.USER_NAME))
        assert wait.until(EC.visibility_of_element_located(locators.BTN_ENTER_REG))
        assert wait.until(EC.url_to_be(BASE_URL))
