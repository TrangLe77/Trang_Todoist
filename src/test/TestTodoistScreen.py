from selenium import webdriver
import unittest
from appium import webdriver


class TestTodoistScreen(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # self.dc['app'] = "/Users/trang.le/Downloads/todoist-v9782.apk"
        self.dc['uuid'] = "emulator-5554"
        self.dc['appPackage'] = "com.todoist"
        self.dc['appActivity'] = "com.todoist.activity.HomeActivity"
        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'Pixel 2'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    # def tearDown(self):
    #     time.sleep(Constants.MINIMUM_TIME_OUT)
    #     self.driver.quit()
