import time

from Pages.Basepage import Basepage
from Pages.Homepage import homepage
from Tests.test_base import BaseTest
from Utilities.readproperties import Readconfig
from Locators.locators import locators


class loginpage(Basepage):
    username_id = locators.uid
    password_id = locators.Pwd
    Login_btn_id = locators.Loginbtn
    Click_Logout_xpath = locators.Logout_btn
    Menu_Click_xpath = locators.Menu_btn

    def __init__(self,driver):
        super().__init__(driver)

    def get_login(self):
        self.driver.find_element_by_id(self.username_id).send_keys(Readconfig.getUsername())
        self.driver.find_element_by_id(self.password_id).send_keys(Readconfig.getPassword())
        self.driver.find_element_by_id(self.Login_btn_id).click()
        return homepage(self.driver)

    def get_logout(self):
        self.driver.find_element_by_xpath(self.Menu_Click_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Click_Logout_xpath).click()

    def get_page_title(self):
        assert self.driver.title == "Swag Labs"



        # self.driver.find_element_by_id("user-name").send_keys(username)
        # self.driver.find_element_by_id("password").send_keys(password)
        # self.driver.find_element_by_id("login-button").click()
        # self.driver.find_element_by_xpath("//*[@id='react-burger-menu-btn']").click()
        # self.driver.find_element_by_xpath("//*[@id='logout_sidebar_link']").click()