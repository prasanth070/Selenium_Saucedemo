import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_login(self):
    """
    1.Selecting chrome as Browser
    2.Opening the website using url
    3.Enter user_name
    4.Enter password
    5.Click on th login button
    6.Verify title 
    """
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.saucedemo.com/")
    username = self.driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    time.sleep(1)
    password = self.driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    time.sleep(1)
    self.driver.find_element(By.ID,"login-button").click()
    time.sleep(1)
    page_title = self.driver.find_element(By.CLASS_NAME,"app_logo")
    title = page_title.text
    expected_title = "Swag Labs"
    assert expected_title in title
    print("Assertion is successful!!!! and login is done ")


def test_logout(self):
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    self.driver.find_element(By.ID, "logout_sidebar_link").click()


