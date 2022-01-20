from base.base import BaseDriver
from selenium.webdriver.common.by import By


class LogInPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    USERNAME = "ap_email"
    PASSWORD = "ap_password"
    CONTINUE_BUTTON = "continue"
    LOG_IN_BUTTON = "signInSubmit"

    def user_name(self):
        return self.driver.find_element(By.ID, self.USERNAME)

    def password(self):
        return self.driver.find_element(By.ID, self.PASSWORD)

    def continue_button(self):
        return self.wait_element_is_clickable(By.ID, self.CONTINUE_BUTTON)
        # return self.driver.find_element(By.ID, self.CONTINUE_BUTTON)

    def log_in_button(self):
        return self.wait_element_is_clickable(By.ID, self.LOG_IN_BUTTON)
        # return self.driver.find_element(By.ID, self.LOG_IN_BUTTON)

    def log_in_with_credentials(self, username, password):
        self.user_name().send_keys(username)
        self.continue_button().click()
        self.password().send_keys(password)
        self.log_in_button().click()
