import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()
