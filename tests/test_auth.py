from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import allure


@allure.feature('Authentication')
class TestAuth:
    @allure.title('valid log in')
    def test_login(self, browser: webdriver.Remote):
        browser.get('https://en.wikipedia.org/w/index.php?title=Special:UserLogin')
        input_username = browser.find_element(By.CSS_SELECTOR, "#wpName1")
        input_username.send_keys('invalid')
        input_password = browser.find_element(By.CSS_SELECTOR, "#wpPassword1")
        input_password.send_keys('invalid')
        button_login = browser.find_element(By.CSS_SELECTOR, "#wpLoginAttempt")
        button_login.click()
        try:
            browser.find_element(By.CSS_SELECTOR, "#pt-anonuserpage")
            assert False, 'anonymous user icon did not disappear'
        except NoSuchElementException:
            pass
