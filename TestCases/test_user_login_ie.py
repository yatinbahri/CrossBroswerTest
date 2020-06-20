from Resources.EnvironmentSetup import BaseSpecificationsIe
import unittest


class Login_to_Employee_ie(BaseSpecificationsIe):

    def test_navigate_to_url(self):
        self.driver.get("https://www.youtube.com")
        title = self.driver.title
        assert title == "YouTube"

if __name__=='__main__':
    unittest.main()