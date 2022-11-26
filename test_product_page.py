import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
list_of_failed_num = [7]
tested_links = [f"{link}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{link}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="known bug", strict=True)
                             )
                for i in range(10)]

@pytest.mark.parametrize("link", tested_links)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.success_add_message_should_be_present()
    page.should_be_product_name_in_cart()
    page.cart_total_should_equal_product_price()