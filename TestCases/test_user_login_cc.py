from Resources.EnvironmentSetup import BaseSpecificationsChrome
import pytest
import unittest


class Login_to_Employee_ie(BaseSpecificationsChrome):

    def test_navigate_to_url(self):
        self.driver.get("https://www.google.com")
        title = self.driver.title
        assert title == "Google"

if __name__ == "__main__":
    unittest.main()


