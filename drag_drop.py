from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(30)
driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
actions = ActionChains(driver)
column_a = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")


actions.drag_and_drop(column_a, target).perform()


input("")
