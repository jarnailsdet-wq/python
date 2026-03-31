# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        # Ensure you have geckodriver installed for Firefox
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10) # Reduced wait time for efficiency
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://qa.lemniska.com/")
        
        # Updated find_element syntax
        driver.find_element(By.ID, "dropdownMenuButton").click()
        
        # Entering Email (handling the typo sequence in your original script)
        email_field = driver.find_element(By.ID, "Email")
        email_field.clear()
        email_field.send_keys("qdu@yopmail.com")
        
        # Entering Password
        pass_field = driver.find_element(By.ID, "Password")
        pass_field.clear()
        pass_field.send_keys("YOUR_PASSWORD_HERE") # Replace '.....' with actual password
        
        # Toggle Remember Me (Cleaned up redundant clicks)
        driver.find_element(By.ID, "RememberMe").click()
        
        # Clicking Login
        driver.find_element(By.ID, "loginBttn").click()
    
    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException: 
            return False
        return True
    
    def is_alert_present(self):
        try: 
            self.driver.switch_to.alert # Modern syntax
        except NoAlertPresentException: 
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: 
            self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()