

import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_login_success(self, driver):
        email = 'm@mmmm.mm'
        password = 'Mmmmm123'

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_ENTER).click()

        wait = WebDriverWait(driver, 10)

        avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
        user_name = wait.until(EC.presence_of_element_located(locators.USER_NAME))

        EXPECTED_URL = 'https://qa-desk.stand.praktikum-services.ru/login'

        wait.until(EC.url_contains('/login'))
        cur_url = driver.current_url

        assert avatar
        assert cur_url == EXPECTED_URL
        assert 'User' in user_name.text
