import time

from selenium.webdriver.common.by import By

from base.base_driver import Base_Driver
from utilities.utils import Utils

# contact us page class
class Contact_Us_Page(Base_Driver):

    # logger
    log = Utils.custom_logger()

    # constructor

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # locators with their values
    first_name_field = "first_name"
    last_name_field = "last_name"
    email_field = "email"
    comment_field = "message"
    submit_button = "//input[@value='SUBMIT']"
    error_message_field = "//body"


    # methods which needs to be used inside test method

    def validate_error_message(self):

        return  self.driver.find_element(By.XPATH, self.error_message_field).text

    def enter_invalid_details_on_contact_us_form(self,fname,lname,email,comment):
        self.log.info("Enter username")
        time.sleep(2)
        self.driver.find_element(By.NAME, self.first_name_field).send_keys(fname)
        self.log.info("Enter lastname")
        time.sleep(2)
        self.driver.find_element(By.NAME, self.last_name_field).send_keys(lname)
        self.log.info("Enter email")
        time.sleep(2)
        self.driver.find_element(By.NAME, self.email_field).send_keys(email)
        self.log.info("Enter comment")
        time.sleep(2)
        self.driver.find_element(By.NAME, self.comment_field).send_keys(comment)
        self.log.info("Click  submit")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.submit_button).click()







