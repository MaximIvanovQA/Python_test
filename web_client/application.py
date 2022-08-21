# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 20.08.2022 11:06
# @My Git  : https://github.com/MaximIvanovQA/Python_test

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from web_client.session import Session


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(60)
        self.session = Session(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

    def closeBrowsers(self):
        self.driver.quit()