import time
import pytest
from pages.contact_us_page import Contact_Us_Page
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data
import softest


# test class of contact us form
@pytest.mark.usefixtures("set_up")
@ddt
class Test_Contact_Us(softest.TestCase):

    # log object used to put log information
    log = Utils.custom_logger()

    # this will be executed before every test method
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.contact_us = Contact_Us_Page(self.driver);



    # test method

    # @data(("abc","xyz","abc@ab","helloworld"),("def","ghi","jkl@ab","helloworldtwo"))
    # @unpack
    @file_data("../testdata/testdata.json")
    def test_registration_form(self,fname,lname,email,comment):

        #contact_us = Contact_Us_Page(self.driver);

        self.contact_us.enter_invalid_details_on_contact_us_form(fname, lname, email, comment)

        # Validate message
        self.log.info("Verify error message")
        text = self.contact_us.validate_error_message()
        assert text == "Erro: Invalid email address"





