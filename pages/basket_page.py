from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def is_basket_empty_text_presented(self):
        text = self.get_element(*BasketPageLocators.CONTENT_INNER)
        assert text, "Text block is not presented"
        assert "Ваша корзина пуста" in text.text, "Text is not correct"
