#check boxes selection of terms and condition
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/checkboxes")
wait = WebDriverWait(driver, 10)
driver.maximize_window()

checkboxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))
print(checkboxes)

ch1=checkboxes[0]
ch2=checkboxes[1]

print(f"ch1----------::::>>> {ch1.is_selected()}")
print(f"ch2----------::::>>> {ch2.is_selected()}")
time.sleep(4)
ch1.click()

if ch1.is_selected():
    print("Checkbox one is selected")
else:
    print("Not selected")    

