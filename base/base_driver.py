
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base_Driver():
    def __init__(self,driver):
        self.driver = driver


    def wait_presence_of_element_located(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.presence_of_element_located(locator_type,locator))
        return element


