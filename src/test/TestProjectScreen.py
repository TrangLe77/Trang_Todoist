import time

from src.screen.MainScreen import MainScreen
from src.screen.ProjectScreen import ProjectScreen
from src.test.TestLogIn import TestSignUpSignInScreen
from src.utils import Constants

from src.data import User
from src.test.TestTodoistScreen import TestTodoistScreen
from src.screen.SignInScreen import SignInScreen


class TestProjectScreen(TestSignUpSignInScreen):
    __testCase = [
        "\n" + "*** testCanCreateNewProjectSuccessfully ***",

    ]

    def _openNewProjectScreen(self):
        signin = self._SignIn()
        time.sleep(Constants.MAXIMUM_TIME_OUT)
        signin.project("Test01")
        new_project = ProjectScreen(self.driver)
        self.assertTrue(new_project.check_page_loaded_after_create())
        return new_project

    def testCanCreateNewProjectSuccessfully(self):
        print(self.__testCase.__getitem__(0))
        self._openNewProjectScreen()

