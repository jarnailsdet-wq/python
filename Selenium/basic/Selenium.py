#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
#
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
print(driver.title)
driver.find_element(By.ID, "username").click()
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(2)
driver.find_element(By.ID, "password").click()
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
message = driver.find_element(By.ID, "flash").text
print(f"Massage : {message}")
driver.quit()

