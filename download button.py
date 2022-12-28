from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(30)

downloadButton = driver.find_element("id", "downloadButton")
downloadButton.click()


progress_label = driver.find_element("class name", "progress-label")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), 'Complete!'
        )
)


input("")
driver.quit()
