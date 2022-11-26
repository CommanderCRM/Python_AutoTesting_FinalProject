import pytest
import time
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

list_of_failed_num = [7]
tested_links = [f"{link}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{link}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="known bug", strict=True)
                             )
                for i in range(10)]

# @pytest.mark.parametrize("link", tested_links)

class TestUserAddToCartFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())[-9:]
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_product_to_cart()
        page.success_add_message_should_be_present()
        page.should_be_product_name_in_cart()
        page.cart_total_should_equal_product_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.success_message_should_disappear()

prod_page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, prod_page_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, prod_page_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_product_to_cart()
        page.success_add_message_should_be_present()
        page.should_be_product_name_in_cart()
        page.cart_total_should_equal_product_price()

def test_guest_cant_see_success_message(browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, prod_page_link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.should_be_no_items_in_cart()
    cart_page.should_be_empty_cart_message()