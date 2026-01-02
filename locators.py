
from selenium.webdriver.common.by import By

BTN_ENTER_REG = (By.XPATH, "//button[text()='Вход и регистрация']")
BTN_NO_ACC = (By.XPATH, "//button[text()='Нет аккаунта']")
BTN_ENTER = (By.XPATH, "//button[text()='Войти']")
BTN_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
BTN_CREATE_ACC = (By.XPATH, "//button[text()='Создать аккаунт']")
BTN_CREATE_AD = (By.XPATH, "//button[text()='Разместить объявление']")
BTN_PUBLISH_AD = (By.XPATH, "//button[text()='Опубликовать']")
BTN_HAS_ACC = (By.XPATH, "//button[text()='Уже есть аккаунт']")
BTN_USER_AVATAR = (By.CSS_SELECTOR, 'button.circleSmall')

RADIO_NEW = (By.XPATH, "//label[contains(text(), 'Новый')]")
RADIO_USED = (By.XPATH, "//label[contains(text(), 'Б/У')]")

INPUT_EMAIL = (By.NAME, 'email')
INPUT_PASSWORD = (By.NAME, 'password')
INPUT_REPEAT_PASSWORD = (By.NAME, 'submitPassword')
INPUT_NAME = (By.NAME, 'name')
INPUT_PRICE = (By.NAME, 'price')
TEXTAREA_DESC = (By.XPATH, '//textarea[@name=\'description\' and @placeholder=\'Описание товара\']')
EMAIL_ERROR_WRAP = (By.XPATH, "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]")
PASSWORD_ERROR_WRAP = (By.XPATH, "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]")
REPEAT_PASSWORD_ERROR_WRAP = (By.XPATH, "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]")





DROPDOWN_CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button[@type='button']")
DROPDOWN_CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button[@type='button']")

USER_AVATAR = (By.CLASS_NAME, 'circleSmall')
USER_NAME = (By.CSS_SELECTOR, 'h3.profileText.name')

POPUP_AUTH_TITLE = (By.XPATH, "//h1[contains(@class,'h1') and contains(., 'Чтобы разместить объявление')]")

REG_ERROR_TEXT = (By.XPATH, "//span[contains(@class, 'input_span') and text()='Ошибка']")

PROFILE_TITLE_MY_ADS = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
PROFILE_PAGINATION_NEXT = (By.CSS_SELECTOR, 'button.arrowButton--right')
PROFILE_PAGINATION_COUNTER = (By.XPATH, "//p[contains(@class,'spanGlobal') and contains(normalize-space(), 'из')]")
PROFILE_CARD_TITLES = (By.CSS_SELECTOR, 'div.card h2.h2')
PROFILE_FIRST_CARD_TITLE = (By.CSS_SELECTOR, 'div.card h2.h2')


