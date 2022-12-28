from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/slider/#custom-handle")
driver.maximize_window()
driver.implicitly_wait(4)

# first we change a frame
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

# make a variable to change a the number
switch_number = driver.find_element(By.ID, "custom-handle")

# switch the number
action = ActionChains(driver)


action.drag_and_drop_by_offset(switch_number, 50, 0).perform()



input("")