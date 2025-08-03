import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_setup():
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.open("https://duckduckgo.com/")

    yield
    browser.quit()

