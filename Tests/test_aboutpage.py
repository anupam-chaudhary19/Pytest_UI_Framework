import time
import pytest

from Pages import Aboutpage
from Pages.Loginpage import loginpage
from Pages.Basepage import Basepage
from Pages.Homepage import homepage
from Pages.Aboutpage import aboutpage
from Tests.test_base import BaseTest


class Test_aboutpage(BaseTest):
    def test_aboutpage(self):
        self.loginpage = loginpage(self.driver)
        self.loginpage.get_login()
        # self.Aboutpage = aboutpage(self.driver)
        aboutpage.get_About_title()



