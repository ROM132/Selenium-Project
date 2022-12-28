from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()
driver.implicitly_wait(30)

num_add = random.randint(10, 20)
num_remove = random.randint(1, 20)

add = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
for i in range(num_add + 1):
    add.click()

time.sleep(4)
remove = driver.find_element("id", 'elements')
for i in range(num_remove + 1):
    try:
        remove.click()
    except:
        print("Can't remove==========================================================================================================")



input("")
