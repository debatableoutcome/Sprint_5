
import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_logout_success(self, driver):
        email = 'm@mmmm.mm'
        password = 'Mmmmm123'
        EXPECTED_URL_AFTER_LOGOUT = 'https://qa-desk.stand.praktikum-services.ru/'

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_ENTER).click()

        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
        wait.until(EC.presence_of_element_located(locators.USER_NAME))

        wait.until(EC.url_contains('/login'))


        driver.find_element(*locators.BTN_LOGOUT).click()
        cur_url = driver.current_url

        absent_avatar = wait.until(EC.invisibility_of_element_located(locators.USER_AVATAR))
        absent_user_name = wait.until(EC.invisibility_of_element_located(locators.USER_NAME))
        assert absent_avatar
        assert absent_user_name
        assert cur_url == EXPECTED_URL_AFTER_LOGOUT
        assert wait.until(EC.presence_of_element_located(locators.BTN_ENTER_REG))

