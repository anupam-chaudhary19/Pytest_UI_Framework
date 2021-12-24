import time

from Pages.Loginpage import loginpage
from Pages.Basepage import Basepage
from Pages.Homepage import homepage
from Tests.test_base import BaseTest


class Test_Homepage(BaseTest):
    def test_homepage(self):
        self.loginpage = loginpage(self.driver)
        homepage= self.loginpage.get_login()
        homepage.get_product1_details()
        time.sleep(5)
        homepage.get_product2_details()
        homepage.get_product3_details()
        time.sleep(5)
        homepage.get_product4_details()
        homepage.get_product5_details()
        homepage.get_product6_details()
        time.sleep(5)

    def test_homepage_title(self):

        homepage.get_homepage_title(self)

    def test_homepage_add_to_cart(self):
        homepage.get_homeproduct1_cart(self)
        time.sleep(5)
        homepage.get_homeproduct2_cart(self)
        homepage.get_homeproduct3_cart(self)
        homepage.get_main_cartdetails(self)
        time.sleep(5)
