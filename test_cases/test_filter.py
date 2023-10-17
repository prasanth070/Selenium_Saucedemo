import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from test_cases.Test_login import test_login
from test_cases.Test_login import test_login , test_logout

class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
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
        page_title = self.driver.find_element(By.CLASS_NAME, "app_logo")
        title = page_title.text
        expected_title = "Swag Labs"
        assert expected_title in title
        print("Assertion is successful!!!! and login is done ")

        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"product_sort_container\"]").click()

        actual_product = self.driver.find_element(By.ID,"item_3_title_link").text
        expected_product_title = "Test.allTheThings() T-Shirt (Red)"
        assert expected_product_title in actual_product
        print(actual_product)

        # self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        # self.driver.find_element(By.ID, "logout_sidebar_link").click()
        test_logout(self)
        time.sleep(2)


    def test_add_cart(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://www.saucedemo.com/")
        # username = self.driver.find_element(By.ID, "user-name")
        # username.send_keys("standard_user")
        # time.sleep(1)
        # password = self.driver.find_element(By.ID, "password")
        # password.send_keys("secret_sauce")
        # time.sleep(1)
        # self.driver.find_element(By.ID, "login-button").click()
        # time.sleep(1)
        # page_title = self.driver.find_element(By.CLASS_NAME, "app_logo")
        # title = page_title.text
        # expected_title = "Swag Labs"
        # assert expected_title in title
        # print("Assertion is successful!!!! and login is done ")
        test_login(self)

        self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

        cart_title = self.driver.find_element(By.CLASS_NAME,"title").text
        expected_text = "Your Cart"
        assert expected_text in cart_title

        cart_itme = self.driver.find_element(By.CLASS_NAME,'inventory_item_name').text
        expected_item_text = "Sauce Labs Backpack"
        assert expected_item_text in cart_itme
        print(cart_itme)

        self.driver.find_element(By.ID,"remove-sauce-labs-backpack").click()

        # self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        # self.driver.find_element(By.ID, "logout_sidebar_link").click()
        test_logout(self)
        time.sleep(2)

