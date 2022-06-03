from selenium.webdriver.common.by import By


class TaskLocator(object):
    TASK_ID = (By.ID, "text")
    COMPLETED_TASK_BOX = (By.XPATH, "(//android.widget.CheckBox[@content-desc=\"Complete\"])[1]")

    # COMPLETED_TASK_BOX = (By.XPATH, "(//android.widget.CheckBox[@content-desc=\"Complete\"])[1]")

    COMPLETED_BAR = (By.ID, "snackbar_text")
    UNDO_BUTTON = (By.ID, "snackbar_action")



