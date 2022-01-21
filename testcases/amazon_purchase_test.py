import pytest
import softest
from pages.home_page.home_page import HomePage
from pages.login_page.log_in_page import LogInPage
from utilities.utilities import Utilities
from ddt import ddt, unpack, data


@pytest.mark.usefixtures("setup")
@ddt
class TestLogIn(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home = HomePage(self.driver)
        self.sign_in = LogInPage(self.driver)
        self.utl = Utilities()

    path = "C:\\Python\\SeleniumProject\\AmazonProject\\testdata\\test_data.xlsx"
    sheet = "Sheet1"
    utl = Utilities()

    @data(*utl.read_data_from_excelfile(path, sheet))
    @unpack
    def test_purchase(self, username, password):
        self.home.click_on_sign_in_button()
        self.sign_in.log_in_with_credentials(username, password)
        self.home.category_drop_down_selection("Baby")
        self.home.iterm_search("Apple iPhone 11 (256GB) - Green")
        self.home.searched_items_selected("Apple iPhone 11 (256GB) - Green")
        self.home.delivery_address("Dhanush S", "7025567614", "686503", "Parambil,Moozhoor, Kottayam", "Kottayam")
        self.home.sign_out()