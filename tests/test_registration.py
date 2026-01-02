
import random
import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    def test_reg_success(self, driver):
        email = f'user_{random.randint(1000, 9999)}@mail.ru'
        password = 'Password123'
        EXPECTED_URL = 'https://qa-desk.stand.praktikum-services.ru/regiatration'

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.BTN_NO_ACC).click()

        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.INPUT_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_CREATE_ACC).click()

        wait = WebDriverWait(driver, 10)

        avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
        user_name = wait.until(EC.presence_of_element_located(locators.USER_NAME))

        wait.until(EC.url_contains('/regiatration'))
        cur_url = driver.current_url

        assert avatar
        assert cur_url == EXPECTED_URL
        assert 'User' in user_name.text

    def test_reg_invalid_email_fail(self, driver):
        email = 'bad_email'


        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.BTN_NO_ACC).click()

        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)

        driver.find_element(*locators.BTN_CREATE_ACC).click()

        wait = WebDriverWait(driver, 10)

        email_wrap = wait.until(EC.presence_of_element_located(locators.EMAIL_ERROR_WRAP))
        pwd_wrap = wait.until(EC.presence_of_element_located(locators.PASSWORD_ERROR_WRAP))
        rep_wrap = wait.until(EC.presence_of_element_located(locators.REPEAT_PASSWORD_ERROR_WRAP))

        error_text = wait.until(EC.presence_of_element_located(locators.REG_ERROR_TEXT))

        email_class = email_wrap.get_attribute('class')
        pw_class = pwd_wrap.get_attribute('class')
        pw_repeat_class = rep_wrap.get_attribute('class')

        assert 'input_inputError' in email_class
        assert 'input_inputError' in pw_class
        assert 'input_inputError' in pw_repeat_class
        assert error_text.text == 'Ошибка'

    def test_reg_existing_acc_no_account_fail(self, driver):
        email = 'm@mmmm.mm'
        password = 'Mmmmm123'

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.BTN_NO_ACC).click()

        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.INPUT_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_CREATE_ACC).click()

        wait = WebDriverWait(driver, 10)

        email_wrap = wait.until(EC.presence_of_element_located(locators.EMAIL_ERROR_WRAP))
        pwd_wrap = wait.until(EC.presence_of_element_located(locators.PASSWORD_ERROR_WRAP))
        rep_wrap = wait.until(EC.presence_of_element_located(locators.REPEAT_PASSWORD_ERROR_WRAP))

        error_text = wait.until(EC.presence_of_element_located(locators.REG_ERROR_TEXT))

        email_class = email_wrap.get_attribute('class')
        pw_class = pwd_wrap.get_attribute('class')
        pw_repeat_class = rep_wrap.get_attribute('class')

        assert 'input_inputError' in email_class
        assert 'input_inputError' in pw_class
        assert 'input_inputError' in pw_repeat_class
        assert error_text.text == 'Ошибка'

