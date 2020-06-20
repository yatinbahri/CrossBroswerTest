from selenium import webdriver
import unittest


class BaseSpecificationsChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/CrossBrowserTest/Resources/chromedriver.exe")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class BaseSpecificationsFirefox(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox(executable_path="C:/Users/User/PycharmProjects/CrossBrowserTest/Resources/geckodriver.exe")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class BaseSpecificationsIe(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Ie(executable_path="C:/Users/User/PycharmProjects/CrossBrowserTest/Resources/IEDriverServer.exe")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()