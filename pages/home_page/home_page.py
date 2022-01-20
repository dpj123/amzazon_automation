import time

from selenium.webdriver.common.by import By
from base.base import BaseDriver
from utilities.utilities import Utilities


class HomePage(BaseDriver):
    utiles = Utilities()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    SIGN_IN = "nav-link-accountList"
    SEARCH_ELEMENT = "twotabsearchtextbox"
    ITEM_AUTOCOMPLE_LIST = "//div[@class='autocomplete-results-container']/div"
    CATEGORY_DROP_DOWN = "searchDropdownBox"
    SEARCH_BUTTON = "nav-search-submit-button"
    SEARCH_ITEM_LIST = "//div[@class='sg-col-inner']/div/div/h2/a"
    ADD_TO_CART = "add-to-cart-button"
    PROCEED_TO_CHECKOUT_BUTTON = "attach-sidesheet-checkout-button"
    COUNTRY = "address-ui-widgets-countryCode-dropdown-nativeId"
    FULL_NAME = "address-ui-widgets-enterAddressFullName"
    MOBILE_NO = "address-ui-widgets-enterAddressPhoneNumber"
    PIN_CODE = "address-ui-widgets-enterAddressPostalCode"
    HOUSE_NAME = "address-ui-widgets-enterAddressLine1"
    TOWN = "address-ui-widgets-enterAddressCity"
    STATE = "//*[@id='address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId']"
    STATE_LIST = "(//div[@id='a-popover-2'])/div/div/ul/li"
    SUBMIT = "address-ui-widgets-form-submit-button"
    DELIVER_TO_ADDRESS = "a-button-inner"
    PAYMENT = "pp-LV7MzC-83"

    def sign_in(self):
        return self.wait_element_is_clickable(By.ID, self.SIGN_IN)

    def search_items(self):
        return self.wait_element_is_clickable(By.ID, self.SEARCH_ELEMENT)

    def item_list(self):
        return self.driver.find_elements(By.XPATH, self.ITEM_AUTOCOMPLE_LIST)

    def category_drop_down(self):
        return self.select_drop_down_value(self.driver.find_element(By.ID, self.CATEGORY_DROP_DOWN))

    def click_on_sign_in_button(self):
        self.action_chain(self.sign_in()).click().perform()

    def click_on_search_button(self):
        return self.wait_element_is_clickable(By.ID, self.SEARCH_BUTTON)

    def search_item_list(self):
        return self.driver.find_elements(By.XPATH, self.SEARCH_ITEM_LIST)

    def add_into_cart(self):
        return self.wait_element_is_clickable(By.ID, self.ADD_TO_CART)
        # return self.driver.find_element(By.ID, self.ADD_TO_CART)

    def proceed_to_check_out(self):
        return self.wait_element_is_clickable(By.ID, self.PROCEED_TO_CHECKOUT_BUTTON)

    def full_name(self):
        return self.driver.find_element(By.ID, self.FULL_NAME)

    def mobile_no(self):
        return self.driver.find_element(By.ID, self.MOBILE_NO)

    def pin_code(self):
        return self.driver.find_element(By.ID, self.PIN_CODE)

    def house_name(self):
        return self.driver.find_element(By.ID, self.HOUSE_NAME)

    def town(self):
        return self.driver.find_element(By.ID, self.TOWN)

    def state(self):
        state_locator = self.driver.find_element(By.XPATH, self.STATE)
        return self.select_drop_down_value(state_locator)

    def state_list(self):
        return self.driver.find_elements(By.XPATH, self.STATE_LIST)

    def submit_button(self):
        return self.wait_element_is_clickable(By.ID, self.SUBMIT)

    def deliver_to_this_address(self):
        return self.driver.find_element(By.CLASS_NAME, self.DELIVER_TO_ADDRESS)

    def country(self):
        country_locator = self.driver.find_element(By.ID, self.STATE)
        return self.select_drop_down_value(country_locator)

    def payment(self):
        return self.wait_element_is_clickable(By.ID, self.PAYMENT)

    def iterm_search(self, item):
        self.search_items().send_keys(item)
        self.click_on_search_button().click()

    def category_drop_down_selection(self, selected_item):
        select = self.category_drop_down()
        option_list = select.options
        item_selection = self.utiles.custom_drop_down_selection(option_list, selected_item)
        select.select_by_visible_text(item_selection)

    def searched_items_selected(self, selected_one):
        search_item_list = self.search_item_list()
        parent_window = self.driver.current_window_handle
        item = self.utiles.select_item_from_the_list(search_item_list, selected_one)
        item.click()
        child_windows = self.driver.window_handles
        window = self.utiles.window_handle(parent_window, child_windows)
        self.driver.switch_to.window(window)
        self.add_into_cart().click()
        self.proceed_to_check_out().click()

    def delivery_address(self, name, mobile, pin, house, town):
        self.full_name().send_keys(name)
        self.mobile_no().send_keys(mobile)
        self.pin_code().send_keys(pin)
        self.house_name().send_keys(house)
        self.town().send_keys(town)
        self.submit_button().click()
        time.sleep(5)
