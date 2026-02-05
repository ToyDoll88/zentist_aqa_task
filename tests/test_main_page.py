import allure
from config import links_count
from pages.main_page import MainPage


@allure.title('Main page content')
def test_main_page_content(page, base_url):
    main_page = MainPage(page, base_url)

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Verify main page has title'):
        assert main_page.get_title() != ""

    with allure.step('Verify main page has "Fork me" link'):
        assert main_page.has_fork_me_link()

    with allure.step('Count links'):
        assert main_page.count_links() == links_count
