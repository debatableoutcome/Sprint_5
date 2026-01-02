import time

import locators
from mock_data import GOOD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCreateAd:
    def test_create_ad_unauth_popup_shows(self, driver):
        driver.find_element(*locators.BTN_CREATE_AD).click()
        popup_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.POPUP_AUTH_TITLE)
        )
        assert popup_title.text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_create_ad_auth_user_success(self, driver):
        email = 'm@mmmmm.mm'
        password = 'Mmmmm123'

        unique_suffix = str(int(time.time()))
        ad_title = f'{GOOD["Название"]} {unique_suffix}'

        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(locators.BTN_ENTER_REG)).click()
        wait.until(EC.element_to_be_clickable(locators.INPUT_EMAIL)).send_keys(email)
        wait.until(EC.element_to_be_clickable(locators.INPUT_PASSWORD)).send_keys(password)
        wait.until(EC.element_to_be_clickable(locators.BTN_ENTER)).click()

        wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
        wait.until(EC.presence_of_element_located(locators.USER_NAME))

        wait.until(EC.element_to_be_clickable(locators.BTN_CREATE_AD)).click()
        wait.until(EC.element_to_be_clickable(locators.INPUT_NAME)).send_keys(ad_title)

        wait.until(EC.element_to_be_clickable(locators.DROPDOWN_CATEGORY_ARROW)).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//button[.//span[contains(text(), \'{GOOD["Категория"]}\')]]')
            )
        ).click()

        if GOOD['Состояние товара'] == 'Б/У':
            wait.until(EC.element_to_be_clickable(locators.RADIO_USED)).click()
        else:
            wait.until(EC.element_to_be_clickable(locators.RADIO_NEW)).click()

        wait.until(EC.element_to_be_clickable(locators.DROPDOWN_CITY_ARROW)).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//button[.//span[contains(text(), \'{GOOD["Город"]}\')]]')
            )
        ).click()

        desc = wait.until(EC.presence_of_element_located(locators.TEXTAREA_DESC))
        driver.execute_script('arguments[0].scrollIntoView({block: \'center\'});', desc)

        desc.click()
        desc.click()
        desc.click()
        desc.clear()
        desc.send_keys(GOOD['Описание'])

        price = wait.until(EC.element_to_be_clickable(locators.INPUT_PRICE))
        price.click()
        price.send_keys(str(GOOD['Стоимость']))

        wait.until(EC.element_to_be_clickable(locators.BTN_PUBLISH_AD)).click()
        wait.until(EC.invisibility_of_element_located(locators.BTN_PUBLISH_AD))

        wait.until(EC.element_to_be_clickable(locators.BTN_USER_AVATAR))
        driver.find_element(*locators.BTN_USER_AVATAR).click()

        wait.until(EC.presence_of_element_located(locators.PROFILE_TITLE_MY_ADS))

        card_title_locator = (
            By.XPATH,
            f"//h2[contains(@class,'h2') and normalize-space()='{ad_title}']"
        )

        card = None
        max_pages = 10

        for _ in range(max_pages):
            titles = driver.find_elements(*card_title_locator)
            if titles:
                card = titles[0].find_element(
                    By.XPATH,
                    "./ancestor::div[contains(@class,'card')]"
                )
                break

            next_buttons = driver.find_elements(*locators.PROFILE_PAGINATION_NEXT)
            if not next_buttons:
                break

            next_btn = next_buttons[0]
            if not next_btn.is_enabled() or next_btn.get_attribute('disabled'):
                break

            first_title_before = driver.find_element(
                *locators.PROFILE_FIRST_CARD_TITLE
            ).text

            next_btn.click()

            wait.until_not(
                EC.text_to_be_present_in_element(
                    locators.PROFILE_FIRST_CARD_TITLE,
                    first_title_before
                )
            )

        assert card is not None

        price_locator = (
            By.XPATH,
            ".//div[contains(@class,'price')]//h2[contains(@class,'h2')]"
        )
        price_text = card.find_element(*price_locator).text

        digits = ''.join(ch for ch in price_text if ch.isdigit())
        assert digits == str(GOOD['Стоимость'])
