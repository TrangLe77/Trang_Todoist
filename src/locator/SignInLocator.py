from selenium.webdriver.common.by import By


class SignInLocator(object):
    CONTINUE_WITH_EMAIl_BUTTON_1 = (By.ID, "btn_welcome_email")
    EMAIL_FIELD = (By.ID, "email_exists_input")
    CONTINUE_WITH_EMAIl_BUTTON_2 = (By.ID, "btn_continue_with_email")
    SIGN_UP_NAME_INPUT = (By.ID, "sign_up_name")
    SIGN_UP_PASSWORD_INPUT = (By.ID, "sign_up_password")
    PASSWORD_INPUT = (By.ID, "log_in_password")
    SIGN_UP_BUTTON = (By.ID, "btn_sign_up")
    TERM_BUTON = (By.ID, "terms_button")
    LOGIN_BUTTON = (By.ID, "btn_log_in")
    NO_CHANGE_TIMEZONE = (By.ID, "button2")
    ERROR_MESSAGE = (By.ID, "dialogViewMessage")
    HELLO_THEME = (By.ID, "theme_picker_hello")
    HOW_TO_PLAN_YOUR_DAY_TEXT = (By.ID, "empty_help_link")
    # MENU_BUTTON = (By.XPATH, "//android.widget.ImageButton[@content-desc=\"Menu\"]")
    MENU_BUTTON = "Menu"
    ADD_PROJECT_BUTTON = (By.ID, "add")
    PROJECT_NAME_FILED = (By.ID, "name")
    COLOR = (By.ID, "form_color")
    GREEN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                       "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                       "ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                       "RecyclerView/android.widget.TextView[7]")
    PARENT = (By.ID, "parent")
    WELCOME = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                         "ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/"
                         "androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]")
    FAVORITE = (By.ID, "form_favorite")
    LIST_VIEW = (By.ID, "list_view_radio")
    BOARD_VIEW = (By.ID, "board_view_radio")
    SUBMIT_BUTTON = (By.ID, "menu_form_submit")
    ADD_TASK_BUTTON = (By.ID, "fab")
    TASK_TITLE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                            "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/"
                            "android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                            ".FrameLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget."
                            "ScrollView/android.widget.LinearLayout/android.widget.EditText[1]")
    TASK_DESCRIPTION = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                                  "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                                  "ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                                  "ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget."
                                  "LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[2]")
    TODAY = (By.ID, "schedule")
    # TODAY = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
    #                    "android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
    #                    "FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
    #                    "android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]")
    SCHEDULE_BUTTON = (By.ID, "scheduler_submit")
    INBOX = (By.ID, "project")
    SUBMIT_TASK_BUTTON = "Add"





