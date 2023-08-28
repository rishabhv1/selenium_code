from selenium.webdriver.common.by import By

from base.base_driver import Base_Driver
from pages.ebay_help_page import Ebay_Help_Page
from utilities.utils import Utils


class Ebay_Home_Page(Base_Driver):

    log = Utils.custom_logger()

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    help_and_contact_field = "//a[@class='gh-p'][normalize-space()='Help & Contact']"



    def click_on_help_and_contact_link(self):
        self.log.info("Click on help and contact link")
        self.driver.find_element(By.XPATH, self.help_and_contact_field).click()
        help_page_obj = Ebay_Help_Page(self.driver)
        return help_page_obj
