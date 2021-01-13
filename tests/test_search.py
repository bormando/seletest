from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time


@allure.feature('Search')
class TestSearch:
    @allure.title('search finds results')
    def test_search_finds_results(self, browser: webdriver.Remote):
        browser.get('https://en.wikipedia.org')
        input_field = browser.find_element(By.CSS_SELECTOR, 'input#searchInput')
        input_field.send_keys('selenium in testing')
        input_field.send_keys(Keys.ENTER)
        results = browser.find_elements(By.CSS_SELECTOR, ".mw-search-result")
        results_number = len(results)
        # time.sleep(3)
        assert results_number > 0, F"expected to find any results"
