"""
These tests cover DuckDuckGo searches.
"""
import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    f = open('testfile', 'a')

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()
    f.write('result_page search input: ' + result_page.search_input_value() + '\n')


    # And the search result links pertain to "panda"
    titles_1 = []
    for title in result_page.result_link_titles():
        assert phrase[0:3].lower() in title.lower()
        titles_1.append(title)

    # And the search result title contains "panda"
    assert phrase in result_page.title()
    f.write('result page title: ' + result_page.title() + '\n')

    # When the first result is clicked
    # Then the correct URL is loaded
    assert result_page.result_link_open() is True

    # When clicking Back button
    browser.back()

    # Then return to search results
    assert browser.current_url == search_page.search_url()

    # And search results are the same
    titles_2 = []
    for title in result_page.result_link_titles():
        titles_2.append(title)
    f.write('titles before: ' + ','.join(titles_1) + '\n' + 'titles after: ' + ','.join(titles_2) + '\n')
    assert titles_1 == titles_2

    # Given user clicks 'More results'
    result_page.more_results()

    # Then new search results are loaded
    titles_more = []
    for title in result_page.result_link_titles():
        titles_more.append(title)
    assert len(titles_more) > len(titles_2)
    f.write('Less results: ' + str(len(titles_2)) + '\n')
    f.write('More results: ' + str(len(titles_more)))

    # And they also pertain to "panda"
    titles_new = set(titles_more) - set(titles_2)
    for title in titles_new:
        assert phrase[0:3].lower() in title.lower()

    f.close()
