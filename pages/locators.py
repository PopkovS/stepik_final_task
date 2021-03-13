from selenium.webdriver.common.by import By

class Links():
    MAIN_LINK = "http://lk.pub.ast.safib.ru/"
    AUTHORIZATION_LINK = MAIN_LINK + "Account/Login"


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FIELD_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FIELD_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"][value=\"Register\"]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#id_quantity+.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE_ON_PAGES_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs:nth-child(2)")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-safe.alert-noicon.alert-success:nth-child(1) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default[href]")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")


class AuthorizationAndRegistrationLocators():
    EMAIL_FIELD = (By.CSS_SELECTOR, "#Email[name=\"Email\"]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#PasswordUser[name=\"PasswordUser\"]")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.block.full-width.m-b")
