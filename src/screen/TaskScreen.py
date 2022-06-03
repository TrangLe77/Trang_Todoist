from src.locator.TaskLocator import TaskLocator
from src.screen.TodoistScreen import TodoistScreen
from src.utils import Constants
import time



class TaskScreen(TodoistScreen):
    __action = [
        "* __verify_display_task: expected: {}, actual: {}   *",
        "* __click_complete_task_box *",
        "* __verify_display_completed_text: expected: {}, actual: {}   *",
        "* __click_undo_task *",

    ]

    def __init__(self, driver):
        self.locator = TaskLocator
        super().__init__(driver)

    def __verify_display_task(self, text):
        actual = self.find_element(*self.locator.TASK_ID).text
        print(self.__action.__getitem__(0).format(text, actual))
        return True if text == actual else False

    def __click_complete_task_box(self):
        print(self.__action.__getitem__(1))
        self.click_element(*self.locator.COMPLETED_TASK_BOX)

    def __verify_display_completed_text(self, com):
        actual = self.find_element(*self.locator.COMPLETED_BAR).text
        print(self.__action.__getitem__(2).format(com, actual))
        return True if com == actual else False

    def __click_undo_task(self):
        print(self.__action.__getitem__(3))
        self.click_element(*self.locator.UNDO_BUTTON)

    def check_page_loaded_after_create_task(self):
        return self.__verify_display_task("Meeting with Singapore side")

    def completion(self):
        self.__click_complete_task_box()

    def reopen(self):
        self.__click_complete_task_box()
        self.__click_undo_task()

    def check_completed_task(self):
        return self.__verify_display_completed_text("Completed.")

    def check_reopened_task(self):
        return self.__verify_display_task("Meeting with Singapore side")
