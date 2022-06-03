import time

from src.locator.SignInLocator import SignInLocator
from src.screen.TodoistScreen import TodoistScreen
from src.utils import Constants


class MainScreen(TodoistScreen):
    __action = [
        "* __verify_theme: expected: {}, actual: {}   *",
        "* __verify_how_to_plan_your_day_text: expected: {}, actual: {}   *",
        "* __click_menu_button *",
        "* __click_add_button *",
        "* __input_project_name: {} *",
        "* __click_color_button *",
        "* __select_green_color *",
        "* __click_parent_button *",
        "* __select_welcome *",
        "* __select_favorite *",
        "* __click_submit_button *",
        "* __click_add_task_button *",
        "* __input_task_title: {} *",
        "* __input_task_description: {} *",
        "* __click_today_button *",
        "* __click_reschedule_button *",
        "* __click_submit_task_button *",



    ]

    def __init__(self, driver):
        self.locator = SignInLocator
        super().__init__(driver)

    def __verify_theme(self):
        actual = self.find_element(*self.locator.HELLO_THEME) is not None
        print(self.__action.__getitem__(0).format(True, actual))
        return True if actual else False

    def __verify_how_to_plan_your_day_text(self):
        actual = self.find_element(*self.locator.HOW_TO_PLAN_YOUR_DAY_TEXT) is not None
        print(self.__action.__getitem__(1).format(True, actual))
        return True if actual else False

    def __click_menu_button(self):
        print(self.__action.__getitem__(2))
        self.click_element_by_accessibility_id(self.locator.MENU_BUTTON)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def __click_add_button(self):
        print(self.__action.__getitem__(3))
        self.click_element(*self.locator.ADD_PROJECT_BUTTON)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def __input_project_name(self, name):
        print(self.__action.__getitem__(4).format(name))
        self.find_element(*self.locator.PROJECT_NAME_FILED).send_keys(name)

    def __click_color_button(self):
        print(self.__action.__getitem__(5))
        self.click_element(*self.locator.COLOR)

    def __select_green_color(self):
        print(self.__action.__getitem__(6))
        self.click_element(*self.locator.GREEN)

    def __click_parent_button(self):
        print(self.__action.__getitem__(7))
        self.click_element(*self.locator.PARENT)

    def __select_welcome(self):
        print(self.__action.__getitem__(8))
        self.click_element(*self.locator.WELCOME)

    def __select_favorite(self):
        print(self.__action.__getitem__(9))
        self.click_element(*self.locator.FAVORITE)

    def __click_submit_button(self):
        print(self.__action.__getitem__(10))
        self.click_element(*self.locator.SUBMIT_BUTTON)

    def __click_add_task_button(self):
        print(self.__action.__getitem__(11))
        self.click_element(*self.locator.ADD_TASK_BUTTON)

    def __input_task_title(self, title):
        print(self.__action.__getitem__(12).format(title))
        self.find_element(*self.locator.TASK_TITLE).send_keys(title)

    def __input_task_description(self, des):
        print(self.__action.__getitem__(13).format(des))
        self.find_element(*self.locator.TASK_DESCRIPTION).send_keys(des)

    def __click_today_button(self):
        print(self.__action.__getitem__(14))
        self.click_element(*self.locator.TODAY)

    def __click_reschedule_button(self):
        print(self.__action.__getitem__(15))
        self.click_element(*self.locator.SCHEDULE_BUTTON)

    def __click_submit_task_button(self):
        print(self.__action.__getitem__(16))
        self.click_element_by_accessibility_id(self.locator.SUBMIT_TASK_BUTTON)

    def project(self, name):
        self.__click_menu_button()
        self.__click_add_button()
        self.__input_project_name(name)
        self.__click_color_button()
        self.__select_green_color()
        self.__click_parent_button()
        self.__select_welcome()
        self.__select_favorite()
        self.__click_submit_button()

    def task(self, title, des):
        self.__click_add_task_button()
        self.__input_task_title(title)
        self.__input_task_description(des)
        self.__click_today_button()
        self.__click_reschedule_button()
        self.__click_submit_task_button()
        self.driver.back()

    def check_page_loaded_after_sign_up(self):
        return self.__verify_theme()

    def check_page_loaded_after_sign_in(self):
        return self.__verify_how_to_plan_your_day_text()
