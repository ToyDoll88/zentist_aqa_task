import allure

from pages.base_page import BasePage
import logging


class LoginPage(BasePage):
    PATH = "/login"

    USERNAME = '#username'
    PASSWORD = '#password'
    LOGIN_BUTTON = 'button[type="submit"]'
    ERROR_MESSAGE = '#flash'

    @allure.step("Login with username '{username}' and password '{password}'")
    def login(self, username: str, password: str):
        logging.info('Fill "username"')
        self.page.fill(self.USERNAME, username)

        logging.info('Fill "password"')
        self.page.fill(self.PASSWORD, password)

        logging.info('Click login button')
        self.page.click(self.LOGIN_BUTTON)

    @allure.step("Get login error message")
    def get_error_message(self) -> str:
        logging.info('Read error message')
        return self.page.locator(self.ERROR_MESSAGE).inner_text()
