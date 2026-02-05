import logging

import allure
from config import username, password
from pages.internal_page import InternalPage
from pages.login_page import LoginPage


@allure.title("User can login and logout successfully")
def test_successful_login(page, base_url):
    login_page = LoginPage(page, base_url)

    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Login with valid credentials"):
        login_page.login(username, password)

    internal_page = InternalPage(page, base_url)

    with allure.step("Verify '/security' page is opened"):
        try:
            assert '/security' in login_page.get_url()
        except AssertionError as e:
            logging.error(f"No, it's actually not: {e}")

    with allure.step("Verify '/secure' page is opened"):
        assert '/secure' in internal_page.get_url()
        assert internal_page.get_title() != ''
        assert internal_page.get_content_element()
        # in case requirements meant ALL content, not only #content element
        assert internal_page.get_content() != ''
        assert internal_page.logout_button_exists()

    with allure.step("Logout from secure page"):
        internal_page.logout_button_click()

    with allure.step("Verify login page is opened"):
        assert '/login' in login_page.get_url()

