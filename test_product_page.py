from time import sleep

import pytest

from .pages.product_page import ProductPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize('numlink', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, numlink):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{numlink}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket_from_product_page()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_page()
