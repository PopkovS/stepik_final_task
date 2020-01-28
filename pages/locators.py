from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#id_quantity+.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE_ON_PAGES_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs:nth-child(2)")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-safe.alert-noicon.alert-success:nth-child(1) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default[href]")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
