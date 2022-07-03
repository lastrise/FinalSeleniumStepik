import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.basket
@pytest.mark.guest
@pytest.mark.main_page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.is_basket_empty()
    basket.is_basket_empty_text_presented()


@pytest.mark.login
@pytest.mark.guest
@pytest.mark.main_page
class TestLoginFromMainPage:

    url = "http://selenium1py.pythonanywhere.com"

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.url)
        page.open()
        page.should_be_login_link()
