from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not presented in URL"

    def should_be_login_form(self):
        assert self.get_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.get_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_form = self.get_element(*LoginPageLocators.REGISTER_FORM)
        email_input = register_form.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        password_input = register_form.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_confirm_input = register_form.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT)
        button = register_form.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        button.click()

        self.is_not_element_present(*LoginPageLocators.INNER_ALERT, 20)

    def authorize_user(self, email, password):
        login_form = self.get_element(*LoginPageLocators.LOGIN_FORM)
        email_input = login_form.find_element(*LoginPageLocators.LOGIN_EMAIL)
        password_input = login_form.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        button = login_form.find_element(*LoginPageLocators.LOGIN_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        button.click()

        self.is_not_element_present(*LoginPageLocators.INNER_ALERT, 20)