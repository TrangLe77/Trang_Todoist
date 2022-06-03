from selenium.webdriver.common.by import By


class ProjectLocator(object):
    MENU_BUTTON = "Menu"
    PROJECT_ID = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                            "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/"
                            "android.widget.FrameLayout[3]/android.view.ViewGroup/androidx.recyclerview.widget."
                            "RecyclerView/android.widget.RelativeLayout[8]/android.widget.TextView")
    VERIFY_PROJECT = (By.ID, "empty_text")


