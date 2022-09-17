from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//*[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="passowrd"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/1')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgot password?')
    PASSWORD_INPUT_ERROR_MSG = (By.XPATH, '//*[text()="Please enter your password!"]')
    SIGN_UP_LINK = (By.XPATH, '//*[text()="Sign up."]')


    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')
        sleep(3)

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(3)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        sleep(3)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        sleep(3)

    def click_sign_up_link(self):
        self.driver.find_element(*self.SIGN_UP_LINK).click()
        sleep(3)

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
        sleep(3)


