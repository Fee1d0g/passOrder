from selenium.webdriver.common.by import By
from pages.base import BaseFunction


class MainPage(BaseFunction):
    search_box_main = (By.XPATH, '//androidx.cardview.widget.CardView\
    [@resource-id="com.paytalab.mkseo.passorder:id/btn_search_query"]/android.widget.LinearLayout')

    def click_search_box_main_page(self):
        self.click_by_locator(self.search_box_main)