from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignUpPage(BasePage):
    PERSONAL_BUTTON = (By.XPATH, '//input[@value="personal"]')
    CONTINUE_BUTTON = (By.XPATH, '//span[@class="MuiButton-label" and text ()= "CONTINUE"]')
    FIRST_NAME_INPUT= (By.XPATH, '//*[@placeholder="Type your answer here..."]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@placeholder="Type your answer here..."]')
    EMAIL_INPUT = (By.XPATH, '//*[@placeholder="Type your answer here..."]')
    PASSWORD = (By.XPATH, '[contains(text(),"password...")]')
    WRONG_EMAIL = (By.XPATH, '//*[text()="Please enter a valid email address."]')

    def navigate_page(self):
        self.driver.get('https://jules.app/sign-up')
        sleep(3)

   # def click_sign_up_page(self):
   #    self.driver.find_element(*self.SIGN_UP).click()
   #    sleep(3)

    def click_personal_account(self):
        self.driver.find_element(*self.PERSONAL_BUTTON).click()
        sleep(3)

    def click_continue_btn(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(3)

    def set_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        sleep(3)


    def set_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        sleep(3)

    def set_emai(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(3)

    def verify_email_error_msg_is_displayed(self):
        actual = self.driver.find_element(*self.WRONG_EMAIL).text
        expected = "Please enter a valid email address."
        self.assertEqual(expected, actual, 'Email error message is NOT displayed')
        sleep(3)

    def verify_password_confirmation_text(self):
        actual = self.driver.find_element(*self.PASSWORD).text
        expected = "password..."
        self.assertEqual(expected, actual, 'Password text confirmation missing')
        sleep(3)

    
