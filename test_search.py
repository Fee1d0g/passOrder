import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.main import MainPage
from pages.search import SearchPage
from pages.store import StorePage


class TestScenario(unittest.TestCase):
    def setUp(self):
        appium_server_url = "http://localhost:4724"
        capabilities = UiAutomator2Options().load_capabilities({
            'platformName': 'Android',
            'platformVersion': '11.0',
            'deviceName': 'Android',
            'noReset': True
        })
        self.driver = webdriver.Remote(appium_server_url, options=capabilities)
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.store_page = StorePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_scenario(self):
        keyword = "cafe"

        self.main_page.click_search_box_main_page()  # 메인 화면 - 검색 화면 이동
        self.search_page.click_search_box_search_page()  # 검색 화면의 검색창 클릭
        self.search_page.search_keyword(keyword)  # 검색창에 키워드 입력
        self.search_page.click_store_item_1()  # 검색 결과 중 첫번째 매장 클릭
        time.sleep(2)
        self.store_page.check_store_name(keyword)  # 매장 상세 정보 화면의 이름과 검색어 비교
        self.store_page.click_back_button_store_page()  # 매장 상세 정보 화면 - 검색 화면 이동
        self.search_page.click_back_button_search_page()  # 검색 화면 - 메인 화면 이동
