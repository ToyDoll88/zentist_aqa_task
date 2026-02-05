import pytest
from playwright.sync_api import sync_playwright
from config import BASE_URL


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default=BASE_URL)
    parser.addoption("--headless", action="store_true")
    parser.addoption("--browser", action="store", default="chromium",
                     choices=["chromium", "firefox", "webkit"])


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base_url")


@pytest.fixture(scope="session")
def headless(pytestconfig):
    return pytestconfig.getoption("--headless")


@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, headless, browser_name):
    if browser_name == "chromium":
        browser = playwright_instance.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright_instance.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright_instance.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unknown browser: {browser_name}")

    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
