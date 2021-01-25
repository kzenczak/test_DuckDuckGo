"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class DuckDuckGoResultPage:
    # Locators
    RESULT_URL_DOMAIN = (By.CLASS_NAME, 'result__url__domain')
    RESULT_URL_FULL = (By.CLASS_NAME, 'result__url__full')
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    MORE_RESULTS = (By.CSS_SELECTOR, '.result--more__btn')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    # Fetch results titles
    def results_url(self):
        result_url = self.browser.find_element(*self.RESULT_URL_DOMAIN).text + self.browser.find_element(*self.RESULT_URL_FULL).text
        return result_url

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    # Click a result and check if correct URL is loaded
    def result_link_open(self):
        result_url = self.results_url()
        result_link = self.browser.find_element(By.CSS_SELECTOR, 'a.result__a')
        result_link.click()
        new_url = self.browser.current_url
        return True if result_url == new_url else False

    # Check if search phrase is the same
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    # Click more results button
    def more_results(self):
        self.browser.implicitly_wait(5)
        more_results_button = self.browser.find_element(*self.MORE_RESULTS)
        more_results_button.click()

    # Page title
    def title(self):
        return self.browser.title
