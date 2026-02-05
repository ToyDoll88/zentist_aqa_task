import allure
import logging


class BasePage:
    PATH = ''

    FORK_ME = 'img[alt="Fork me on GitHub"]'
    CONTENT = '#content'

    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    @allure.step("Get current url")
    def get_url(self) -> str:
        logging.info("Get current url")
        return self.page.url

    @allure.step("Find page's title")
    def get_title(self) -> str:
        logging.info("Get page's title")
        return self.page.title()

    @allure.step("'Fork me on GitHub' is visible")
    def has_fork_me_link(self) -> bool:
        logging.info("Find 'Fork me on GitHub' element")
        return self.page.locator(self.FORK_ME).is_visible()

    @allure.step("Find content element")
    def get_content_element(self) -> bool:
        logging.info("Find content element")
        return self.page.locator(self.CONTENT).is_visible()

    @allure.step("Get whole page content")
    def get_content(self) -> str:
        logging.info("Get whole page content")
        return self.page.content()

    @allure.step(f"Open page {PATH}")
    def open(self):
        logging.info(f"Go to {self.base_url + self.PATH}")
        self.page.goto(self.base_url + self.PATH)
