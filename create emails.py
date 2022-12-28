from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


class create_account:
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://jqueryui.com/dialog/#modal-form")
    driver.maximize_window()
    driver.implicitly_wait(4)

    
    def __init__(self, num):
        # make the account details
        self.name = None
        self.email = None
        self.password = None

        self.num = num



    def create_details(self):
        # switch frame
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

        # click on the create new user button
        button_create_user = self.driver.find_element(By.ID, "create-user")
        button_create_user.click()


        # make the names emails and passwords
        names = ["rom", "shon", "agam", "poli"]
        emails = ["rom.adenayev", "shon.ade", "agam.adenayev", "poli.adenayev"]
        passwords = ["rom1234", "shon1234", "agam1234", "poli1234"]

        name = names[self.num]
        email = emails[self.num]
        password = passwords[self.num]

        # delete all the thing that in the field already
        name_to_delete = self.driver.find_element(By.ID, "name")
        name_to_delete.clear()

        email_to_delete = self.driver.find_element(By.ID, "email")
        email_to_delete.clear()

        password_to_delete = self.driver.find_element(By.ID, "password")
        password_to_delete.clear()

        # fill the field with the name, email and password
        name_to_delete.send_keys(name)

        email_to_delete.send_keys(f"{email}@gmail.com")

        password_to_delete.send_keys(password)

        # submit all 
        submit_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Create an account'])[1]")
        submit_button.click()

        # end the switch frame
        self.driver.switch_to.default_content()

if __name__ == "__main__":
    for i in range(15):
        num = input("Enter the number of the account: ")
        num = int(num)  # convert input string to integer
        c = create_account(num)
        c.create_details()