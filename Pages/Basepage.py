from selenium import webdriver
import pytest

# This class is parent of all the pages and contains generic methods and all utilities

class Basepage:
    def __init__(self, driver):
        self.driver = driver