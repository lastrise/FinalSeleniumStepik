from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "[href=\"/ru/basket/\"]")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM = (By.CLASS_NAME, "register_form")
    LOGIN_FORM = (By.CLASS_NAME, "login_form")

    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")

    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=\"login_submit\"]")

    INNER_ALERT = (By.CSS_SELECTOR, "div.alertinner")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    INNER_ALERT = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    CONTENT_INNER = (By.ID, "content_inner")
