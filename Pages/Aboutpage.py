import time

from Pages.Basepage import Basepage
from Pages.Homepage import homepage
from Pages.Loginpage import loginpage
from Tests.test_base import BaseTest
from Utilities.readproperties import Readconfig
from Locators.locators import locators


class aboutpage(Basepage):
    Click_About_xpath = locators.About_btn
    Menu_Click_xpath = locators.Menu_btn

    def __init__(self,driver):
        super().__init__(driver)

    def get_About_title(self):
        self.driver.find_element_by_xpath(self.Menu_Click_xpath).click()
        self.driver.find_element_by_xpath(self.Click_About_xpath).click()
        self.driver.back()
        pagetitle = "Swag Labs"
        if self.driver.title == pagetitle:
            print("Test passed")
        else:
            print("Test failed")

