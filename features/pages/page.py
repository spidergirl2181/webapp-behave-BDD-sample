from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from features.pages.locator import Locator


class Page(object):
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.implicit_wait = 30

    def wait_till_DOM_loaded(self):
        try:
            ready_check = self.browser.execute_script('return document.readyState == "complete"')
            self.browser.WebDriverWait.until(ready_check,"DOM is fully loaded")
        except TimeoutError:
            raise

    def search_by_keyword(self, keyword):
        try:
            search_box = self.browser.find_element(By.NAME, Locator.SEARCH_BOX)
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.ENTER)
            WebDriverWait(self.browser, self.implicit_wait)
        except:
            print("Search activity can not be performed")  

    def is_serp_display(self):
        WebDriverWait(self.browser, self.implicit_wait)
        serp = self.browser.find_element(By.ID, Locator.SERP_CONTAINER)
        serp_header = self.browser.find_element(By.XPATH, Locator.SERP_HEADER)
        if (serp_header and serp is not None):
            return True

    def content_search(self, keyword):
        content = self.browser.page_source
        return keyword in content

