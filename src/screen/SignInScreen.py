import time

from src.locator.SignInLocator import SignInLocator
from src.screen.MainScreen import MainScreen
from src.screen.TodoistScreen import TodoistScreen
from src.utils import Constants


class SignInScreen(TodoistScreen):
    __action = [
        "* __click_continue_with_email_button_1 *",
        "* __enter_email: {} *",
        "* __click_continue_with_email_button_2 *",
        "* __enter_name: {} *",
        "* __enter_password: {} *",
        "* __click_signup_button *",
        "* __click_terms_button *",
        "* __enter_login_password: {} *",
        "* __click_login_button *",

    ]

    def __init__(self, driver):
        self.locator = SignInLocator
        super().__init__(driver)

    def __click_continue_with_email_button_1(self):
        print(self.__action.__getitem__(0))
        self.click_element(*self.locator.CONTINUE_WITH_EMAIl_BUTTON_1)
        time.sleep(Constants.MAXIMUM_TIME_OUT_10)

    def __enter_email(self, email):
        print(self.__action.__getitem__(1).format(email))
        self.find_element(*self.locator.EMAIL_FIELD).send_keys(email)

    def __click_continue_with_email_button_2(self):
        print(self.__action.__getitem__(2))
        self.click_element(*self.locator.CONTINUE_WITH_EMAIl_BUTTON_2)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def __enter_name(self, name):
        print(self.__action.__getitem__(3).format(name))
        self.find_element(*self.locator.SIGN_UP_NAME_INPUT).send_keys(name)

    def __enter_password(self, password):
        print(self.__action.__getitem__(4).format(password))
        self.find_element(*self.locator.SIGN_UP_PASSWORD_INPUT).send_keys(password)

    def __click_signup_button(self):
        print(self.__action.__getitem__(5))
        self.click_element(*self.locator.SIGN_UP_BUTTON)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def __click_terms_button(self):
        print(self.__action.__getitem__(6))
        self.click_element(*self.locator.TERM_BUTON)

    def __enter_login_password(self, password):
        print(self.__action.__getitem__(7).format(password))
        self.find_element(*self.locator.PASSWORD_INPUT).send_keys(password)

    def __click_login_button(self):
        print(self.__action.__getitem__(8))
        self.click_element(*self.locator.LOGIN_BUTTON)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def signup(self, email, name, password):
        self.__click_continue_with_email_button_1()
        self.__enter_email(email)
        self.__click_continue_with_email_button_2()
        self.__enter_name(name)
        self.__enter_password(password)
        self.__click_signup_button()
        self.__click_terms_button()

    def login(self, email, password):
        self.__click_continue_with_email_button_1()
        self.__enter_email(email)
        self.__click_continue_with_email_button_2()
        self.__enter_login_password(password)
        self.__click_login_button()

    def signup_with_valid_user(self, email, name, password):
        self.signup(email, name, password)
        return MainScreen(self.driver)

    def login_with_valid_user(self, email, password):
        self.login(email, password)
        return MainScreen(self.driver)


