from Resources.EnvironmentSetup import BaseSpecificationsFirefox
import pytest
import unittest

class Login_to_Employee(BaseSpecificationsFirefox):

    def test_navigate_to_url(self):
        self.driver.get("https://www.gmail.com")
        title = self.driver.title
        assert  title == "Gmail"

if __name__ == "__main__":
    unittest.main()