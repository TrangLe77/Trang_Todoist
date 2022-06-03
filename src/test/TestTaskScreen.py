import time

from src.screen.MainScreen import MainScreen
from src.screen.ProjectScreen import ProjectScreen
from src.screen.TaskScreen import TaskScreen
from src.test.TestLogIn import TestSignUpSignInScreen
from src.utils import Constants

from src.data import User
from src.test.TestTodoistScreen import TestTodoistScreen
from src.screen.SignInScreen import SignInScreen


class TestTaskScreen(TestSignUpSignInScreen):
    __testCase = [
        "\n" + "*** testCanCreateTaskSuccessfully ***",
        "\n" + "*** testCanCompleteTaskSuccessfully ***",
        "\n" + "*** testCanReopenTaskSuccessfully ***",

    ]

    def _openTaskScreen(self):
        signin = self._SignIn()
        time.sleep(Constants.MAXIMUM_TIME_OUT)
        signin.task("Meeting with Singapore side", "Discussing about new specifications")
        new_task = TaskScreen(self.driver)
        self.assertTrue(new_task.check_page_loaded_after_create_task())
        return new_task

    def testCanCreateTaskSuccessfully(self):
        print(self.__testCase.__getitem__(0))
        self._openTaskScreen()

    def testCanCompleteTaskSuccessfully(self):
        print(self.__testCase.__getitem__(1))
        completed_task = self._openTaskScreen()
        completed_task.completion()
        self.assertTrue(completed_task.check_completed_task())

    def testCanReopenTaskSuccessfully(self):
        print(self.__testCase.__getitem__(2))
        completed_task = self._openTaskScreen()
        completed_task.reopen()
        self.assertTrue(completed_task.check_reopened_task())


