from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.get_element(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.get_element(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def get_element(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                expected_conditions.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        login_link.click()

    def open(self):
        self.browser.get(self.url)
