from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_ADD_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")