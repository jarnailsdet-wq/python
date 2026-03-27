#ads or alerta handling
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait , Select
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")
wait = WebDriverWait(driver, 10)
driver.maximize_window()
try:
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mdal']/div[2]/div[3]")))
    close_button.click()
    print("Entry ad close successfully")
except Exception as e:
    print(f"Mudal not found : {e}")
finally:
    driver.quit()
            