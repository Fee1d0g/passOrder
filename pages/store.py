from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base import BaseFunction


class StorePage(BaseFunction):
    id_store_name = ["com.paytalab.mkseo.passorder:id/txt_store_name",
                     "com.paytalab.mkseo.passorder:id/txt_store_title"]
    back_button = (By.CLASS_NAME, "android.widget.ImageButton")

    def click_back_button_store_page(self):
        self.click_by_locator(self.back_button)

    def check_store_name(self, keyword):
        for element_id in self.id_store_name:
            try:
                store_name = self.driver.find_element(By.ID, element_id)
                assert keyword.upper() in store_name.text.upper(), f"FAIL: 매장 이름에 검색어 '{keyword}'가 존재하지 않음"
                print(f"PASS: 매장 이름 '{store_name.text}'에서 검색어 '{keyword}' 확인")
                break
            except NoSuchElementException:
                continue
