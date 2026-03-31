#report generation 



from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

import time



# Set up Chrome WebDriver



chrome_options = Options()

chrome_options.add_experimental_option("detach", True)  # This will keep the browser open after the script finishes

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://qa.lemniska.com/")

wait = WebDriverWait(driver, 10)

driver.maximize_window()



##time.sleep(5)



# Click on dropdown sign up button

dropdown_signup = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))

#time.sleep(2)

dropdown_signup.click()

print("Test Case 3 : Dropdown icon is present -Test Case Passed")



# Click on Sign up link

driver.find_element(By.LINK_TEXT, "Sign up").click()

print("Test Case 4 :Sign Up icon is selected -Test Case Passed")

#time.sleep(3.5)



# Assert URL

membersignup_url = driver.current_url

print(f"Current URL: {membersignup_url}")

assert membersignup_url == "http://qa.lemniska.com/membership"

print("Test case 5 : Assert for Member Sign Up page URL is passed")

#time.sleep(2)



# Validate page title

membersignup_title = driver.find_element(By.XPATH, "//h2[normalize-space()='Member Sign Up']").text

assert membersignup_title == "Member Sign Up"

print("Test case 6 : Assert for Member Sign Up Title is passed")



#driver.quit() #------------------------



chrome_options = Options()

chrome_options.add_experimental_option("detach", True)  # This will keep the browser open after the script finishes

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://qa.lemniska.com/")

wait = WebDriverWait(driver, 10)

driver.maximize_window()



##time.sleep(5)



# Click on dropdown sign up button

dropdown_signup = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))

#time.sleep(2)

dropdown_signup.click()

print("Test Case 1 : Dropdown icon is present -Test Case Passed")



# Click on Sign up link

driver.find_element(By.LINK_TEXT, "Sign up").click()

print("Test Case 2 :Sign Up icon is selected -Test Case Passed")

#time.sleep(3.5)



# Assert URL

membersignup_url = driver.current_url

print(f"Current URL: {membersignup_url}")

assert membersignup_url == "http://qa.lemniska.com/membership"

print("Test case 3 : Assert for Member Sign Up page URL is passed")

#time.sleep(2)



# Validate page title

membersignup_title = driver.find_element(By.XPATH, "//h2[normalize-space()='Member Sign Up']").text

assert membersignup_title == "Member Sign Up"

print("Test case 4 : Assert for Member Sign Up Title is passed")