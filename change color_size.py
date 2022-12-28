from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://jqueryui.com/selectmenu/#product-selection")
driver.maximize_window()
driver.implicitly_wait(4)

class class_:
    def __init__(self, size, color):
        self.size = str(size)
        self.id_size = None

        # pick one of this "50", "100", "150", "200", "250"
        if self.size == "50":
            self.id_size = "ui-id-1"
        elif self.size == "100":
            self.id_size = "ui-id-2"
        elif self.size == "150":
            self.id_size = "ui-id-3"
        elif self.size == "200":
            self.id_size = "ui-id-4"
        elif self.size == "250":
            self.id_size = "ui-id-5"
        else:
            driver.quit()

        self.color = color
        self.id_color = None
        # color to pick : Black, Red, Yellow, Blue, Green
        if self.color in ["black", "Black"]:
            self.id_color = "ui-id-6"
        elif self.color in ["red", "Red"]:
            self.id_color = "ui-id-7"
        elif self.color in ["yellow", "Yellow"]:
            self.id_color = "ui-id-8"
        elif self.color in ["blue", "Blue"]:
            self.id_color = "ui-id-9"
        elif self.color in ["green", "Green"]:
            self.id_color = "ui-id-10"
        else:
            driver.quit()

    def change_size(self):
        # change a frame first
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

        # open the option of the circle radius
        circle_radius = driver.find_element(By.ID, "radius-button")
        circle_radius.click()

        # pick the size he/she choose
        pick_size = driver.find_element(By.ID, self.id_size)
        pick_size.click()
        
        # back to the first frame
        driver.switch_to.default_content()

    def change_color(self):
        # change a frame first
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

        # open the option of the circle radius
        circle_color = driver.find_element(By.ID, "color-button")
        circle_color.click()

        # pick the size he/she choose
        pick_color = driver.find_element(By.ID, self.id_color)
        pick_color.click()
        
        # back to the first frame
        driver.switch_to.default_content()



if __name__ == "__main__":
    class_ = class_(250, "black")
    class_.change_size()
    class_.change_color()
    input("")