#drop down

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait , Select
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/dropdown")
wait = WebDriverWait(driver, 10)
driver.maximize_window()

checkboxes = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
time.sleep(3)
dropdown = Select(checkboxes)
time.sleep(5)
dropdown.select_by_visible_text("Option 1")
time.sleep(3)
dropdown.select_by_value("2")
time.sleep(5)
print(checkboxes)