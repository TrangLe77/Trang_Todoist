from src.locator.ProjectLocator import ProjectLocator
from src.screen.TodoistScreen import TodoistScreen
from src.utils import Constants
import time



class ProjectScreen(TodoistScreen):
    __action = [
        "* __click_menu_button *",
        "* __verify_display_project: expected: {}, actual: {}   *",



    ]

    def __init__(self, driver):
        self.locator = ProjectLocator
        super().__init__(driver)

    def __click_menu_button(self):
        print(self.__action.__getitem__(0))
        self.click_element_by_accessibility_id(self.locator.MENU_BUTTON)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def __verify_display_project(self, text):
        actual = self.find_element(*self.locator.PROJECT_ID).text
        print(self.__action.__getitem__(1).format(text, actual))
        return True if text == actual else False

    def check_page_loaded_after_create(self):
        self.__click_menu_button()
        return self.__verify_display_project("Test01")