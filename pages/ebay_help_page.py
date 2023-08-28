from selenium.webdriver.common.by import By

from base.base_driver import Base_Driver
from utilities.utils import Utils


class Ebay_Help_Page(Base_Driver):

    log = Utils.custom_logger()

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    how_can_we_help_header = "//h1[@id='srTil']"



    def get_header_text(self):
        self.log.info("Get the text from the header value")
        return self.driver.find_element(By.XPATH, self.how_can_we_help_header).text
