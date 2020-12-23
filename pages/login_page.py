import time

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Substring 'login' is not presented in \
        login url "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
        "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
        "Register form is not presented"

    def register_new_user(self, email, password):
        enter_email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        enter_email_field.send_keys(email)
        enter_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        enter_password_field.send_keys(password)
        enter_password_repeat_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        enter_password_repeat_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        time.sleep(3)
