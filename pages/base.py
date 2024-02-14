from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BaseFunction:
    def __init__(self, driver):
        self.driver = driver

    def click_by_locator(self, element_locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(element_locator)).click()

    def enter_keyword(self, keyword, element_locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(element_locator)).send_keys(keyword)
        print(f"{keyword}" + " 입력")
