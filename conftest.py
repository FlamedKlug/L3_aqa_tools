import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_setup():
    browser.config.window_width = 800
    browser.config.window_height = 600

    yield
    browser.quit()


@pytest.fixture
def browser_open(browser_setup):
    browser.open("https://duckduckgo.com/")
