from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/resizable/")
driver.maximize_window()
driver.implicitly_wait(4)

action = ActionChains(driver)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

resizable = driver.find_element(By.CLASS_NAME, "ui-icon-gripsmall-diagonal-se")


action.drag_and_drop_by_offset(resizable, 100, 130).perform()

input("click to end: ")
