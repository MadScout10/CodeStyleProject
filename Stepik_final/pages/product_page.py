from selenium.common.exceptions import NoAlertPresentException
from .main_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def check_product_name(self):
        added_prod_name = self.browser.find_element(*ProductPageLocators.NAME_OF_ADDED_PRODUCT)
        x = added_prod_name.text
        real_prod_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        y = real_prod_name.text
        assert x == y, 'Wrong name of added product'
        print('Name checked, all fine')

    def check_price(self):
        added_prod_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_ADDED_PRODUCT)
        x = added_prod_price.text
        real_prod_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        y = real_prod_price.text
        assert x == y, 'Wrong name of added product'
        print('Price checked, all fine')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
        
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
