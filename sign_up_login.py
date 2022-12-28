import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



class Registration:
    def __init__(self, f_name, l_name, email, phone_number, company_name, street_address,
                city, state, postcode, password):

        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.phone_number = phone_number
        self.company_name = company_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postcode = postcode
        self.county = state
        self.mobile_number = phone_number
        self.password = password

    def open_website(self):
        # open the website
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.driver.get("https://phptravels.org/register.php")

        # maximize the size of the windows and wait four second if something is not found
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

        self.action = ActionChains(self.driver)

    def Personal_Information(self):
        # fulfill all the personal information
        first_name = self.driver.find_element(By.ID, "inputFirstName")
        first_name.send_keys(self.f_name)

        last_name = self.driver.find_element(By.ID, "inputLastName")
        last_name.send_keys(self.l_name)

        email = self.driver.find_element(By.ID, "inputEmail")
        email.send_keys(self.email)

        phone_number = self.driver.find_element(By.ID, "inputPhone")
        phone_number.send_keys(self.phone_number)

    def Billing_Address(self):
        # fulfill all the Billing Address
        company_name = self.driver.find_element(By.ID, "inputCompanyName")
        company_name.send_keys(self.company_name)
        
        street_address = self.driver.find_element(By.ID, "inputAddress1")
        street_address.send_keys(self.street_address)

        city = self.driver.find_element(By.ID, "inputCity")
        city.send_keys(self.city)

        state = self.driver.find_element(By.ID, "stateinput")
        state.send_keys(self.state)

        postcode = self.driver.find_element(By.ID, "inputPostcode")
        postcode.send_keys(self.postcode)

        county = self.driver.find_element(By.XPATH, "(//select[@id='inputCountry'])[1]")
        self.action.click(county).send_keys(self.county).send_keys(Keys.ENTER).perform()
        
        # whatsapp phone number
        whatsapp_phoneNumber = self.driver.find_element(By.ID, "customfield2")
        whatsapp_phoneNumber.send_keys(self.phone_number)

        # make a random num that decide how much characters it going to have
        num = random.randint(7, 13)

        # store the random password
        storage = ""

        # make a random password
        for i in range(num):
            storage+=random.choice(self.password)

        # show it on the screen
        input_num = 1
        for i in range(2):
            password = self.driver.find_element(By.ID, f"inputNewPassword{input_num}")
            password.send_keys(storage)
            input_num+=1

        # disable the spam messages
        spam_messages = self.driver.find_element(By.XPATH, "(//span[@class='bootstrap-switch-label'])[1]")
        spam_messages.click()

        # check box 
        check_box = self.driver.find_element(By.XPATH, "(//iframe[@title='reCAPTCHA'])[1]")
        check_box.click()

        # submit button
        time.sleep(4)
        submit_button = self.driver.find_element(By.CLASS_NAME, "btn-recaptcha")
        submit_button.click()

if __name__ == "__main__":
    # Registration
    r = Registration("Rom", "Adenayev", "rom.adenayev@gmail.com", "0535318082", "Rommk", "Hazviten",
     "hedera", "israel", "3821240", "qweasdzxcrtyfghvbnuiojhklm.QWEASDZXCRTYFGHVBNUIOPJKLMp123456789!@#$%^&*")
    r.open_website()
    r.Personal_Information()
    r.Billing_Address()




input("")