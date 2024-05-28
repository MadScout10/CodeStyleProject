from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REG_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, "div#messages :nth-child(1).alert-noicon strong")
    PRICE_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, "div#messages :nth-child(3).alert-noicon strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages :nth-child(1)")

class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
