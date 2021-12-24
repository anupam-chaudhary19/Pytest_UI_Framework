import time
import pytest

from Pages.Loginpage import loginpage
from Pages.Basepage import Basepage
from Tests.test_base import BaseTest


class Test_loginpage(BaseTest):
    def test_login(self):
        self.loginpage = loginpage(self.driver)
        self.loginpage.get_login()
        time.sleep(5)
        self.loginpage.get_page_title()
        self.loginpage.get_logout()

    @pytest.mark.parametrize("username, password",
                             [
                                 ("standard_user", "secret_sauce"),
                                 ("problem_user", "secret_sauce"),
                                 ("performance_glitch_user", "secret_sauce")
                             ]
                             )
    def test_login_parametrize(self, username, password):
        assert self.driver.title == "Swag Labs"
        self.driver.find_element_by_id("user-name").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login-button").click()
        self.driver.find_element_by_xpath("//*[@id='react-burger-menu-btn']").click()
        self.driver.find_element_by_xpath("//*[@id='logout_sidebar_link']").click()
