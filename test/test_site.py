import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_s6(browser):
    browser.get('https://demoblaze.com/index.html')
    galsxy_s6 = browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galsxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'


def test_open_2(browser):
    browser.get('https://demoblaze.com/index.html')
    monitor_link = browser.find_element(By.CSS_SELECTOR, """[onclick="byCat('monitor')"]""")
    monitor_link.click()
    time.sleep(2)
    monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 2
