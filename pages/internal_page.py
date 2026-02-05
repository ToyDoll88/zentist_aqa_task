import allure
import logging
from pages.base_page import BasePage


class InternalPage(BasePage):
    PATH = '/secure'

    LOGOUT_BUTTON = 'a[href="/logout"]'

    @allure.step("Find 'Logout' button")
    def logout_button_exists(self) -> bool:
        logging.info("Find logout button")
        return self.page.locator(self.LOGOUT_BUTTON).is_visible()

    @allure.step("Perform logout")
    def logout_button_click(self):
        logging.info("Perform logout")
        self.page.click(self.LOGOUT_BUTTON)
