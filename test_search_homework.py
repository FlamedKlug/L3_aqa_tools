
from selene import browser, be, have, by


def test_successful_search(browser_setup):
    browser.element('[id="searchbox_input"]').should(be.blank).type('yasaka selene github')\
        .press_enter()
    browser.element('html').should(have.text('https://github.com › yashaka › selene'))


def test_unsuccessful_search(browser_setup):
    browser.element('[id="searchbox_input"]').should(be.blank).type('RFGHJTRDF').press_enter()
    browser.element(by.partial_link_text("rfghjtrdf")).click()
    browser.element('[id="react-layout"]').should(have.text('No results found for'))
