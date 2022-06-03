import time

from src.screen.MainScreen import MainScreen
from src.utils import Constants

from src.data import User
from src.test.TestTodoistScreen import TestTodoistScreen
from src.screen.SignInScreen import SignInScreen


class TestSignUpSignInScreen(TestTodoistScreen):
    __testCase = [
        "\n" + "*** testCanSignUpSuccessfully ***",
        "\n" + "*** testCanSignInSuccessfully ***",

    ]

    def _openApp(self):
        return SignInScreen(self.driver)

    def _SignIn(self):
        signin = self._openApp()
        signin.login_with_valid_user(User.USER_EMAIL, User.PASSWORD)
        return MainScreen(self.driver)

    def testCanSignUpSuccessfully(self):
        print(self.__testCase.__getitem__(0))
        signup = self._openApp()
        todoist = signup.signup_with_valid_user(User.SIGN_UP_USER_EMAIL, User.SIGN_UP_NAME, User.PASSWORD)
        time.sleep(Constants.MINIMUM_TIME_OUT)
        self.assertTrue(todoist.check_page_loaded_after_sign_up())

    def testCanSignInSuccessfully(self):
        print(self.__testCase.__getitem__(1))
        todoist = self._SignIn()
        time.sleep(Constants.MINIMUM_TIME_OUT)
        self.assertTrue(todoist.check_page_loaded_after_sign_in())
