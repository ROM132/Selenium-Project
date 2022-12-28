from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.saucedemo.com/?ref=hackernoon.com")
driver.implicitly_wait(30)

user_name = driver.find_element("id", "user-name")
user_name.send_keys("standard_user")
time.sleep(1)

password = driver.find_element("id", "password")
password.send_keys("secret_sauce")
time.sleep(2)

login_button = driver.find_element("id", "login-button")
login_button.click()

items = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-onesie",
         "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-test.allthethings()-t-shirt-(red)"]

item = random.choice(items)
item_button = driver.find_element("id", f"{item}")
item_button.click()
time.sleep(2)

shopping_cart_link = driver.find_element("id", "shopping_cart_container")
shopping_cart_link.click()

checkout_button = driver.find_element("id", "checkout")
checkout_button.click()

first_name = driver.find_element("id", "first-name")
first_name.send_keys("rom")
time.sleep(0.5)

last_name = driver.find_element("id", "last-name")
last_name.send_keys("adenayev")
time.sleep(0.5)

zipcode = driver.find_element("id", "postal-code")
zipcode.send_keys("3821240")
time.sleep(1)

submit_button = driver.find_element("id", "continue")
submit_button.click()
time.sleep(2)

finish_button = driver.find_element("id", "finish")
finish_button.click()
time.sleep(1)

back_home = driver.find_element("id", "back-to-products")
back_home.click()


input("")
driver.quit()
