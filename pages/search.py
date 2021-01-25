"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:
    # URL
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    # Load the URL
    def load(self):
        self.browser.get(self.URL)

    # Input given search phrase and click search button
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_button = self.browser.find_element(By.ID, 'search_button_homepage')
        search_button.click()

    def search_url(self):
        search_url = self.browser.current_url
        return search_url
