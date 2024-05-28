from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD1)
        input_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2)
        confirm_password.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = str(self.browser.current_url)
        assert 'login' in url, '"login" is not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
