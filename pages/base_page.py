from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest


class BasePage(Browser, unittest.TestCase):

    def wait_for_element(self, by, selector):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((by, selector)))

    def test_url(self):
        actual = self.driver.current_url
        expected = 'https://jules.app/sign-in'
        self.assertEqual(actual, expected, 'URL incorrect')








