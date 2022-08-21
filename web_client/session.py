# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 22.08.2022 00:35
# @My Git  : https://github.com/MaximIvanovQA/Python_test
from selenium.webdriver.common.by import By


class Session:
    def __init__(self, app):
        self.app = app

    def login(self, user):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element(by=By.NAME, value="user-name").click()
        driver.find_element(by=By.NAME, value="user-name").clear()
        driver.find_element(by=By.NAME, value="user-name").send_keys(user.user)
        driver.find_element(by=By.NAME, value="password").click()
        driver.find_element(by=By.NAME, value="password").clear()
        driver.find_element(by=By.NAME, value="password").send_keys(user.password)
        driver.find_element(by=By.NAME, value="login-button").click()

    def logout(self):
        driver =self.app.driver
        driver.find_element(by=By.ID, value="react-burger-menu-btn").click()
        driver.find_element(by=By.ID, value="logout_sidebar_link").click()
