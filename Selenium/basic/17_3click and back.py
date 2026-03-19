#
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
print(driver.title)
driver.find_element(By.LINK_TEXT, "A/B Testing").click()  #1
time.sleep(2)
print(driver.title)
time.sleep(2)
t1=driver.find_element(By.ID,"content").text
print(t1)
driver.back()
time.sleep(2)
print(driver.title)   
driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()  #2
time.sleep(2)
print(driver.title)
b2=driver.find_element(By.XPATH,"//button[text()='Add Element']").click()
time.sleep(2)
b3=driver.find_element(By.XPATH,"//button[text()='Delete']").click()
time.sleep(2)