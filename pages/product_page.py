import math

from selenium.common import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class WithBasketButtonPage(BasePage):
    def add_to_basket(self):
        pass

    def is_product_added(self):
        pass

    def is_not_presented_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.INNER_ALERT), \
            "Success message is presented"

    def is_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.INNER_ALERT), \
            "Success message is not disappeared"


class ProductPage(WithBasketButtonPage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def is_product_added(self):
        alert = self.get_element(*ProductPageLocators.INNER_ALERT)
        assert alert is not False, "Addition to basket alert is not presented"

        name = self.get_element(*ProductPageLocators.NAME_PRODUCT)
        assert name is not False, "Name of product is not presented"

        assert f"{name.text} был добавлен в вашу корзину." == alert.text, \
            "Names of product between page and alert are not equals"


class PromoProductPage(ProductPage):

    def alert_answer(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

    def extract_code(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            return

    def add_to_basket(self):
        super().add_to_basket()
        self.alert_answer()
