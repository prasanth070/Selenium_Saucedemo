import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        # test for login
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

    def test_login_fail(self):
        # negative testcase for login
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        time.sleep(1)
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_saue")
        time.sleep(1)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        error_msg = self.driver.find_element(By.CSS_SELECTOR,"h3").text
        exp_error_msg = "Epic sadface: Username and password do not match any user in this service"
        assert exp_error_msg in error_msg


    def test_logout(self):
        # test to log out
        """
            1.Selecting chrome as Browser
            2.Opening the website using url
            3.Enter user_name
            4.Enter password
            5.Click on th login button
            6.Verify title
            7.find logout button and click
            """
        self.test_login()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()


    def test_content_val(self):
        # UI test case for validating the content of the page
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

        sub_title = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
        print(sub_title)
        expected_title = "Products"
        assert expected_title in sub_title, f"Expected title '{expected_title}' not found. Actual title is: '{sub_title}'"

        product_1 = self.driver.find_element(By.ID, "item_4_title_link")
        product1_title = product_1.text
        print(product1_title)
        expected_title1 = "Sauce Labs Backpack"

        # self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        # self.driver.find_element(By.ID, "logout_sidebar_link").click()



    def test_add_cart(self):
        # test to add elements to cart
        self.test_login()

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

        # test_logout(self)

    def test_untitled(self):
        # test to validate the elements of thr cart
        self.test_login()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"product_sort_container\"]").click()
        actual_product = self.driver.find_element(By.ID, "item_3_title_link").text
        expected_product_title = "Test.allTheThings() T-Shirt (Red)"
        assert expected_product_title in actual_product
        print(actual_product)
        # self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        # self.driver.find_element(By.ID, "logout_sidebar_link").click()
        # test_logout(self)
        time.sleep(2)


    def remove_ele_cart(self):
        # test to remove elements in the cart
        self.driver = webdriver.Chrome()
        self.test_login()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_title = self.driver.find_element(By.CLASS_NAME, "title").text
        expected_text = "Your Cart"
        assert expected_text in cart_title
        cart_itme = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
        expected_item_text = "Sauce Labs Backpack"
        assert expected_item_text in cart_itme
        print(cart_itme)
        self.driver.find_element(By.ID,"remove-sauce-labs-bike-light").click()



    def test_order(self):
        # test for placing an order
        self.driver = webdriver.Chrome()
        self.test_login()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_title = self.driver.find_element(By.CLASS_NAME, "title").text
        expected_text = "Your Cart"
        assert expected_text in cart_title
        cart_itme = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
        expected_item_text = "Sauce Labs Backpack"
        assert expected_item_text in cart_itme
        print(cart_itme)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(2)
        text = self.driver.find_element(By.CLASS_NAME, "title").text
        expected = "Checkout: Your Information"
        print(text)
        assert expected in text
        self.driver.find_element(By.ID, "first-name").send_keys("Mani")
        self.driver.find_element(By.ID, "last-name").send_keys("Vusirikala")
        self.driver.find_element(By.ID, "postal-code").send_keys("505222")
        self.driver.find_element(By.ID, "continue").click()
        text1 = self.driver.find_element(By.CLASS_NAME, "title").text
        expected1 = "Checkout: Overview"
        assert expected1 in text1
        self.driver.find_element(By.ID, "finish").click()
        text2 = self.driver.find_element(By.CLASS_NAME, "complete-text").text
        expected2 = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        assert expected2 in text2
        self.driver.find_element(By.ID, "back-to-products").click()

