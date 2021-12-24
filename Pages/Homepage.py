import time
from Pages.Basepage import Basepage
from Locators.locators import locators


class homepage(Basepage):
    Product1_xpath = locators.Product1
    Product2_xpath = locators.Product2
    Product3_xpath = locators.Product3
    Product4_xpath = locators.Product4
    Product5_xpath = locators.Product5
    Product6_xpath = locators.Product6
    Filterproducts_xpath = "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    ApplyFilter_xpath = "//*[@id='header_container']/div[2]/div[2]/span/select/option[3]"
    Return_to_product_xpath = "//*[@id='back-to-products']"
    Product1_id = locators.Add_to_Cart_product1
    Product2_id = locators.Add_to_Cart_product2
    Product3_id = locators.Add_to_Cart_product3
    Product4_id = locators.Add_to_Cart_product4
    Product5_id = locators.Add_to_Cart_product5
    Product6_id = locators.Add_to_Cart_product6

    Product1_test_xpath = "//*[@id='add-to-cart-sauce-labs-backpack']"

    maincart_xpath = locators.maincart_items

    def __init__(self, driver):
        super().__init__(driver)

    def get_product1_details(self):
        self.driver.find_element_by_xpath(self.Product1_xpath).click()
        pagetitle = "Swag Labs"
        if pagetitle == self.driver.title:
            print("******************** Test passed *******************************")
            self.driver.find_element_by_xpath(self.Return_to_product_xpath).click()
            time.sleep(5)

        else:
            print("******************** Test Fail- Page title not matching ***********************")

        # return homepage(self.driver)

    def get_product2_details(self):
        self.driver.find_element_by_xpath(self.Product2_xpath).click()
        pagetitle = "Swag Labs"
        if pagetitle == self.driver.title:
            print("******************** Test passed *******************************")
            self.driver.find_element_by_xpath(self.Return_to_product_xpath).click()

        else:
            print("******************** Test Fail- Page title not matching ***********************")

    def get_product3_details(self):
        self.driver.find_element_by_xpath(self.Product3_xpath).click()
        pagetitle = "Swag Labs"
        if pagetitle == self.driver.title:
            print("******************** Test passed *******************************")
            self.driver.find_element_by_xpath(self.Return_to_product_xpath).click()

        else:
            print("******************** Test Fail- Page title not matching ***********************")

    def get_product4_details(self):
        self.driver.find_element_by_xpath(self.Product4_xpath).click()
        pagetitle = "Swag Labs"
        if pagetitle == self.driver.title:
            print("******************** Test passed *******************************")
            self.driver.find_element_by_xpath(self.Return_to_product_xpath).click()

        else:
            print("******************** Test Fail- Page title not matching ***********************")

    def get_product5_details(self):
        self.driver.find_element_by_xpath(self.Product5_xpath).click()
        pagetitle = "Swag Labs"
        if pagetitle == self.driver.title:
            print("******************** Test passed *******************************")
            self.driver.find_element_by_xpath(self.Return_to_product_xpath).click()

        else:
            print("******************** Test Fail- Page title not matching ***********************")

    def get_product6_details(self):
        self.driver.find_element_by_xpath(self.Product6_xpath).click()
        pagetitle = "Swag Labs"
        if pagetitle == self.driver.title:
            print("******************** Test passed *******************************")
            self.driver.find_element_by_xpath(self.Return_to_product_xpath).click()

        else:
            print("******************** Test Fail- Page title not matching ***********************")

    def get_homepage_title(self):
        assert self.driver.title == "Swag Labs"

    def get_homeproduct1_cart(self):
        self.driver.find_element_by_xpath(self.Product1_test_xpath).click()

    def get_homeproduct2_cart(self):
        self.driver.find_element_by_id(self.Product2_id).click()

    def get_homeproduct3_cart(self):
        self.driver.find_element_by_id(self.Product3_id).click()

    def get_homeproduct4_cart(self):
        self.driver.find_element_by_id(self.Product4_id).click()

    def get_homeproduct5_cart(self):
        self.driver.find_element_by_id(self.Product5_id).click()

    def get_homeproduct6_cart(self):
        self.driver.find_element_by_id(self.Product6_id).click()

    def get_main_cartdetails(self):
        self.driver.find_element_by_xpath(self.maincart_xpath).click()
        time.sleep(10)
