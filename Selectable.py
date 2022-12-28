from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/selectable/")
driver.maximize_window()
driver.implicitly_wait(3)

action = ActionChains(driver)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

# first
item1 = driver.find_element(By.XPATH, "(//li[normalize-space()='Item 1'])[1]")

# last
item7 = driver.find_element(By.XPATH, "(//li[normalize-space()='Item 7'])[1]")





action.move_to_element(item1).click_and_hold().move_to_element(item7).perform()
action.move_by_offset(100, 100).perform()


input("")