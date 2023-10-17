import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from test_cases.test_login import test_login, test_logout



class TestUntitled():

    def test_content_val(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        time.sleep(1)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        page_title = self.driver.find_element(By.CLASS_NAME, "app_logo").text
        expected_title = "Swag Labs"
        assert expected_title in page_title
        print("Assertion is successful!!!! and login is done ")
        # test_login(self)

        sub_title = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text
        print(sub_title)
        expected_title = "Products"
        assert expected_title in sub_title, f"Expected title '{expected_title}' not found. Actual title is: '{sub_title}'"

        product_1 = self.driver.find_element(By.ID,"item_4_title_link")
        product1_title = product_1.text
        print(product1_title)
        expected_title1 = "Sauce Labs Backpack"

        test_logout(self)


