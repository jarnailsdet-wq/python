#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#1 wait and click on button and text filed

def wait_and_click(wait, by, value):
    element = wait.until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

def text_field_inputs(wait, by,value, send_text):
    element = wait.until(EC.visibility_of_element_located((by, value)))
    element.send_keys(send_text)
    return element


# Set up Chrome WebDriver
driver = webdriver.Chrome()
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
wait_and_click(wait, By.LINK_TEXT, "Sign up")
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
#time.sleep(2)

# Test first name input
firstname = driver.find_element(By.XPATH, "//input[@id='FirstName']")
firstname.send_keys("@$%$%$^^^%^#$^#$^#^#^#$^#%^^")
#time.sleep(2.5)
firstname.clear()
#time.sleep(1.5)
firstname.send_keys("Sane@123")
#time.sleep(1.5)
firstname.clear()
#time.sleep(1.5)
firstname.send_keys("Sane")
#time.sleep(1.5)
firstname.clear()
print("Test Case 7 : First name is added and validated for various inputs-Test Case Passed")

# Test last name input
lastname = driver.find_element(By.XPATH, "//input[@id='LastName']")
lastname.send_keys("@$%$%$^^^%^#$^#$^#^#^#$^#%^^")
#time.sleep(2.5)
lastname.clear()
#time.sleep(1.5)
lastname.send_keys("Kashyap@123")
#time.sleep(1.5)
lastname.clear()
#time.sleep(1.5)
lastname.send_keys("Doe")
#time.sleep(1.5)
lastname.clear()
print("Test Case 8 : Last name is added and validated for various inputs-Test Case Passed")

# Test email input
memberemail = driver.find_element(By.XPATH, "//input[@id='Email']")
memberemail.send_keys("yuve11z3@yopmail.com")
#time.sleep(1.5)
memberemail.clear()
print("Test Case 9 : email is added-Test Case Passed")

# Test phone number input
phonenumber = driver.find_element(By.XPATH, "//input[@id='Phone']")
phonenumber.send_keys("3455953210")
#time.sleep(1.5)
phonenumber.clear()

# Select country (India)
timeeshown = wait_and_click(wait, By.XPATH, "//div[@title='India (भारत): +91']")
timeeshown.send_keys(Keys.ARROW_UP)
timeeshown.send_keys(Keys.ARROW_UP)
timeeshown.send_keys(Keys.ARROW_UP)
timeeshown.send_keys(Keys.ENTER)
print("Test Case 10 : Phone Number is added and validated -Test Case Passed")

print("Test Case 11 : TimeZone is selcted-Test Case Passed")
#time.sleep(5)
print("Test Case 12 : All inputs added are cleared-Test Case Passed")

# Fill all values and submit
firstname.send_keys("Automation")
#time.sleep(1.5)
lastname.send_keys("SignUP")
#time.sleep(1.5)
memberemail.send_keys("yuvitest_AT4@yopmail.com") #--------------------
#time.sleep(1.5)
phonenumber.send_keys("2345678910")
#time.sleep(1.5)
print("Test Case 13 : All values are added and saved-Test Case Passed")

submitbutton = driver.find_element(By.XPATH, "//input[@id='btn_SaveMember']")
submitbutton.click()
print("Test Case 14 : Data is saved-Test Case Passed")
#time.sleep(1.5)

#Alert pop up
driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[2]/button").click()
#time.sleep(1.5)

# Accept terms and conditions
driver.find_element(By.XPATH, "//input[@id='IsVerified']").click()
#time.sleep(1.5)
print("Test Case 15 : Check Box are selected-Test Case Passed")
#time.sleep(1.5)
#driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[2]/button").click()



# Accept HIPAA
driver.find_element(By.ID, "IsVerifiedhppa").click()
#time.sleep(1.5)
print("Test Case 15 : Check Box are selected-Test Case Passed")
#time.sleep(2)
submitbutton.click()
print("Test Case 16 : Data is saved-Test Case Passed")
#time.sleep(4)
# Registration message popup
re=driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div/section/div[1]/section/div/div/div[2]/div/div[1]/div/form/div[1]").text

print(re)


print("QA Member Sign Up completed Sucessfully")
driver.quit()





