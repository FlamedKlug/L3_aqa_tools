
from selene import browser, be, have


def test_successful_search(browser_setup):
    browser.element('[id="searchbox_input"]').should(be.blank).type('yasaka selene github')\
        .press_enter()
    browser.element('html').should(have.text('https://github.com › yashaka › selene'))


def test_unsuccessful_search(browser_setup):
    browser.element('[id="searchbox_input"]').should(be.blank).type(
        'BVFGHJIUYTRFGHJTRDFCHGVGHFDGTERTYGFHRTFG').press_enter()
    browser.element('//*[@id="react-layout"]/div/div/div/div[2]/section[1]/div[1]/div/p[2]/a').click()
    browser.element('html').should(have.text('No results found for'))
