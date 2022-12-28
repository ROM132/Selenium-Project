from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/sortable/")
driver.maximize_window()
driver.implicitly_wait(4)

# create frame
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

num = 1
items = []

# create a list with all the item
for i in range(1, 8):
    items.append(f"(//li[normalize-space()='Item {num}'])[1]")
    num += 1

num1 = 0
num2 = 6
action = ActionChains(driver)

# change the location of the item 1-7, 2-6, 3-5 like this
for i in range(1, 8):
    item1 = driver.find_element(By.XPATH, "".join(items[num1]))
    item2 = driver.find_element(By.XPATH, "".join(items[num2]))

    action.drag_and_drop(item2, item1).perform()
    
    num2 -= 1


input("")