# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 22.08.2022 00:58
# @My Git  : https://github.com/MaximIvanovQA/Python_test
from selenium.webdriver.common.by import By

class Inventory:
    def __init__(self, app):
        self.app = app

    def open_product_card(self, item):
        driver = self.app.driver
        driver.find_element(by=By.ID, value=item).click()