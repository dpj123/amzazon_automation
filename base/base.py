from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def action_chain(self, locator):
        action = ActionChains(self.driver)
        locate = action.move_to_element(locator)
        return locate

    def select_drop_down_value(self, locator):
        select = Select(locator)
        return select

    def explicit_wait(self):
        wait = WebDriverWait(self.driver, 10)
        return wait

    def wait_element_is_clickable(self, locator_type, locator):
        # wait = WebDriverWait(self.driver, 10)
        wait = self.explicit_wait()
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
