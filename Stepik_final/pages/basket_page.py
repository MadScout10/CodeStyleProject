from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def empty_basket_check(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is clear"

    def basket_is_empty_mark_check(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is empty printed"
