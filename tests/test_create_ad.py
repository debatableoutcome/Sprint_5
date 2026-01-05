import time

import locators
from mock_data import GOOD, EXISTING_ACC
from config.urls import BASE_URL

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCreateAd:
    def test_create_ad_unauth_popup_shows(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*locators.BTN_CREATE_AD).click()
        popup_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.POPUP_AUTH_TITLE)
        )
        assert popup_title.text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_create_ad_auth_user_success(self, driver):
        email = EXISTING_ACC['email']
        password = EXISTING_ACC['password']

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
                (By.XPATH, f"//button[.//span[text()='{GOOD['Категория']}']]")
            )
        ).click()

        wait.until(EC.element_to_be_clickable(locators.RADIO_USED)).click()

        wait.until(EC.element_to_be_clickable(locators.DROPDOWN_CITY_ARROW)).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[.//span[text()='{GOOD['Город']}']]")
            )
        ).click()

        desc = wait.until(EC.presence_of_element_located(locators.TEXTAREA_DESC))
        desc.clear()
        desc.send_keys(GOOD['Описание'])

        price = wait.until(EC.element_to_be_clickable(locators.INPUT_PRICE))
        price.send_keys(str(GOOD['Стоимость']))

        wait.until(EC.element_to_be_clickable(locators.BTN_PUBLISH_AD)).click()
        wait.until(EC.invisibility_of_element_located(locators.BTN_PUBLISH_AD))

        wait.until(EC.element_to_be_clickable(locators.BTN_USER_AVATAR)).click()
        wait.until(EC.presence_of_element_located(locators.PROFILE_TITLE_MY_ADS))

        card_found = False

        while True:
            titles = driver.find_elements(*locators.PROFILE_CARD_TITLES)
            titles_texts = [t.text.strip() for t in titles]

            if ad_title in titles_texts:
                card_found = True
                break

            next_buttons = driver.find_elements(*locators.PROFILE_PAGINATION_NEXT)
            if not next_buttons:
                break

            next_buttons[0].click()

            wait.until(
                EC.presence_of_all_elements_located(locators.PROFILE_CARD_TITLES)
            )

        assert card_found, 'Карточка не найдена ни на одной странице профиля'

