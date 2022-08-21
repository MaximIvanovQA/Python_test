# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 20.08.2022 11:06
# @My Git  : https://github.com/MaximIvanovQA/Python_test

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(60)

    def open_home_page(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

    def login(self, user):
        driver = self.driver
        driver.find_element(by=By.NAME, value="user-name").click()
        driver.find_element(by=By.NAME, value="user-name").clear()
        driver.find_element(by=By.NAME, value="user-name").send_keys(user.user)
        driver.find_element(by=By.NAME, value="password").click()
        driver.find_element(by=By.NAME, value="password").clear()
        driver.find_element(by=By.NAME, value="password").send_keys(user.password)
        driver.find_element(by=By.NAME, value="login-button").click()

    def logout(self):
        driver =self.driver
        driver.find_element(by=By.ID, value="react-burger-menu-btn").click()
        driver.find_element(by=By.ID, value="logout_sidebar_link").click()

    def closeBrowsers(self):
        self.driver.quit()