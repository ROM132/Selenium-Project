from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://phptravels.com/demo/")
driver.maximize_window()
driver.implicitly_wait(30)

# field the first name
first_name = driver.find_element(By.NAME, "first_name")
first_name.send_keys("Rom")

# field the second name
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Adenayev")

# field the business name
business_name = driver.find_element(By.NAME, "business_name")
business_name.send_keys("Rommk")

# field the email
email = driver.find_element(By.NAME, "email")
email.send_keys("rom.adenayev@gmail.com")

# find what is num1
num1 = driver.find_element("id", "numb1")
# find what is num2
num2 = driver.find_element("id", "numb2")

# find the total of num1 and num2
total = driver.find_element("id", "number")
# enter the total
total.send_keys(f"{int(num1.text) + int(num2.text)}")

# submit all
time.sleep(2)
submit_button = driver.find_element("id", "demo")
submit_button.click()

input("")
