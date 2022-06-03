import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.utils import Constants


class TodoistScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, Constants.MAXIMUM_TIME_OUT).until(
                ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return self.driver.find_element(*locator)

    def find_element_by_accessibility_id(self, accessibility_id):
        return self.driver.find_element_by_accessibility_id(accessibility_id)

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()
        time.sleep(Constants.MINIMUM_TIME_OUT)

    def click_element_by_accessibility_id(self, accessibility_id):
        element = self.find_element_by_accessibility_id(accessibility_id)
        element.click()
        time.sleep(Constants.MINIMUM_TIME_OUT)
