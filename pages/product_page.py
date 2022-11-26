from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"
    
    def success_add_message_should_be_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_MESSAGE), "Success add message is not presented"

    def should_be_product_name_in_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
        assert product_name == product_name_in_cart, "Product name is not equal to product name in cart"
    
    def cart_total_should_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total = self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
        assert product_price == cart_total, "Product price is not equal to cart total"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_MESSAGE), \
            "Success message is presented, but should not be"