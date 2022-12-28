from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/autocomplete/#multiple")
driver.maximize_window()
driver.implicitly_wait(4)

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

entry = driver.find_element(By.ID, "tags")
entry.send_keys("p")
entry.send_keys(Keys.BACKSPACE)


num = 1
try:
    for i in range(50):
        all_text = driver.find_element(By.XPATH, f"(//li[@class='ui-menu-item'])[{num}]")
        num += 1

        entry.send_keys(f"{all_text.text}, ")
        entry.send_keys(Keys.RETURN)
except:
    print("done")


input("")