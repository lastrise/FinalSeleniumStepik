import pytest
import time

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.product
@pytest.mark.guest
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_not_presented_success_message()


@pytest.mark.product
@pytest.mark.guest
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.is_not_presented_success_message()


@pytest.mark.product
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_success_message_disappeared()


@pytest.mark.need_review
@pytest.mark.basket
@pytest.mark.product
@pytest.mark.guest
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.is_basket_empty()
    basket.is_basket_empty_text_presented()


@pytest.mark.need_review
@pytest.mark.guest
@pytest.mark.product
@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


@pytest.mark.need_review
@pytest.mark.guest
@pytest.mark.product
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_product_added()


@pytest.mark.user
@pytest.mark.product
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        password = "123456789AAA"
        email = str(time.time()) + "@fakemail.org"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.is_product_added()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.is_not_presented_success_message()
