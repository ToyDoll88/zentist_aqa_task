import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.title("Navigation to Login page")
def test_navigate_to_login_page(page, base_url):
    main_page = MainPage(page, base_url)

    with allure.step("Open main page"):
        main_page.open()

    with allure.step("Go to login page"):
        main_page.go_to_login()

    with allure.step("Verify URL"):
        assert '/login' in main_page.get_url()


# Negative cases cover most common equivalence classes:
# - invalid username
# - invalid password
# - empty username
# - empty password
@allure.title("Negative login scenarios")
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("wrong", "wrong", "Your username is invalid"),
        ("tomsmith", "wrong", "Your password is invalid"),
        ("", "SuperSecretPassword!", "Your username is invalid"),
        ("tomsmith", "", "Your password is invalid"),
    ]
)
def test_negative_login(page, base_url, username, password, expected_error):
    login_page = LoginPage(page, base_url)

    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Try to login with invalid credentials"):
        login_page.login(username, password)

    with allure.step(f"Verify error message: {expected_error}"):
        assert expected_error in login_page.get_error_message()
