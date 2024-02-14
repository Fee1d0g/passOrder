from selenium.webdriver.common.by import By
from pages.base import BaseFunction


class SearchPage(BaseFunction):
    store_item_1 = (By.XPATH, '(//android.view.ViewGroup[@resource-id="com.paytalab.mkseo.passorder:id/container"])[1]')
    search_box_search_page = (By.ID, "com.paytalab.mkseo.passorder:id/edt_store_query")
    back_button = (By.CLASS_NAME, "android.widget.ImageButton")

    def click_search_box_search_page(self):
        self.click_by_locator(self.search_box_search_page)

    def search_keyword(self, keyword):
        self.enter_keyword(keyword, self.search_box_search_page)

    def click_store_item_1(self):
        self.click_by_locator(self.store_item_1)

    def click_back_button_search_page(self):
        self.click_by_locator(self.back_button)