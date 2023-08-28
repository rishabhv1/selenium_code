
import pytest

from pages.ebay_home_page import  Ebay_Home_Page
from utilities.utils import Utils


@pytest.mark.usefixtures("set_up")
class Test_Ebay_Help():
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.obj = Ebay_Home_Page(self.driver)
        self.help_page_object = self.obj.click_on_help_and_contact_link()

    def test_help_form_header_text(self):
        #obj = Ebay_Home_Page(self.driver)
       # help_page_object = obj.click_on_help_and_contact_link()
        text = self.help_page_object.get_header_text()
        self.log.info("Verify the text")
        assert text == "How can we help you today?"
