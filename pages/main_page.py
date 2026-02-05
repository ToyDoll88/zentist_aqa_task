from pages.base_page import BasePage
import logging
import allure


class MainPage(BasePage):
    PATH = '/'

    LOGIN_LINK = 'a[href="/login"]'
    LINK = '#content ul li a'

    @allure.step("Count links")
    def count_links(self) -> int:
        logging.info("Count links")
        return self.page.locator(self.LINK).count()

    @allure.step('Click on "Form Authentication" element')
    def go_to_login(self):
        logging.info('Click on "Form Authentication" element')
        self.page.click(self.LOGIN_LINK)
