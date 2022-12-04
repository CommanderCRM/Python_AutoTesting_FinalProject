from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_cart_url()

    def should_be_cart_url(self):
        assert "basket" in self.browser.current_url, "Cart link is not presented"

    def should_be_no_items_in_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.ITEMS_IN_CART), "Items are presented in cart, but should not be"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(
            *CartPageLocators.EMPTY_CART_MESSAGE), "Empty cart message is not presented"
