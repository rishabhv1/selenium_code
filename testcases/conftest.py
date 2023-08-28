import os

import pytest
import pytest_html
from selenium import webdriver
from webdriver_manager.core import driver

from utilities.utils import Utils

# this is to be executed before every test class
@pytest.fixture(scope="class")
def set_up(request):
    log = Utils.custom_logger()
    driver = webdriver.Chrome(executable_path = "C:\\Tools\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    log.info("Open ebay website")
    driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    log.info("Close website")
    driver.close()



