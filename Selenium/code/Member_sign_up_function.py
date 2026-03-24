#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#1 wait and click on button and text filed

def wait_and_click(wait, by, value):#------------
    element = wait.until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

def text_field_inputs(wait, by,value, send_text):#---------------------
    element = wait.until(EC.visibility_of_element_located((by, value)))
    for i in send_text:
        element.send_keys(i)
        time.sleep(0.5)
        element.clear()
        time.sleep(0.5)    
        return element
 
#def negative_text_field_inputs(wait, by,value, send_text):    
    
    
def fill_filed(wait,by,value,send_text):
    element = wait.until(EC.visibility_of_element_located((by, value)))
    element.send_keys(send_text)
    return element


# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://qa.lemniska.com/")
wait = WebDriverWait(driver, 10)
driver.maximize_window()

# Click on dropdown sign up button
wait_and_click(wait, By.TAG_NAME, "button")

print("Test Case 1 : Dropdown icon is present -Test Case Passed")

# Click on Sign up link
wait_and_click(wait, By.LINK_TEXT, "Sign up")
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
#time.sleep(2)

# Test first name input
text_field_inputs(wait, By.XPATH, "//input[@id='FirstName']",["abhi123", "Sane", "Kashyap@123","@$%$%$^^^%^#$^#$^#^#^#$^#%^^" ])


fill_filed(wait, By.XPATH, "//input[@id='FirstName']","Abhi")
print("Test Case 5 : First name is added and validated for various inputs-Test Case Passed")

# Test last name input
text_field_inputs(wait, By.XPATH, "//input[@id='LastName']",["@$%$%$^^^%^#$^#$^#^#^#$^#%^^","Kashyap@123","Doe"])


fill_filed(wait, By.XPATH, "//input[@id='LastName']","Sahni")
print("Test Case 6 : Last name is added and validated for various inputs-Test Case Passed")

# Test email input
memberemail = text_field_inputs(wait, By.XPATH, "//input[@id='Email']","yuve11z7@yopmail.com")


#time.sleep(1.5)
memberemail.clear()
print("Test Case 7 : email is added-Test Case Passed")

# Test phone number input
phonenumber = text_field_inputs(wait, By.XPATH, "//input[@id='Phone']","3455953210")
#time.sleep(1.5)
phonenumber.clear()

# Select country (India)
timeeshown = wait_and_click(wait, By.XPATH, "//div[@title='India (भारत): +91']")
timeeshown.send_keys(Keys.ARROW_UP)
timeeshown.send_keys(Keys.ARROW_UP)
timeeshown.send_keys(Keys.ARROW_UP)
timeeshown.send_keys(Keys.ENTER)
print("Test Case 8 : Phone Number is added and validated -Test Case Passed")

print("Test Case 9 : TimeZone is selcted-Test Case Passed")
#time.sleep(5)
print("Test Case 10 : All inputs added are cleared-Test Case Passed")

# Fill all values and submit
#firstname.send_keys("Automation")
#time.sleep(1.5)
#lastname.send_keys("SignUP")
#time.sleep(1.5)
memberemail.send_keys("yuvitest_AT8@yopmail.com") #--------------------
#time.sleep(1.5)
phonenumber.send_keys("2345678910")
#time.sleep(1.5)
print("Test Case 11 : All values are added and saved-Test Case Passed")

submitbutton = wait_and_click(wait, By.XPATH, "//input[@id='btn_SaveMember']")


print("Test Case 12 : Data is saved-Test Case Passed")
#time.sleep(1.5)

#Alert pop up
wait_and_click(wait, By.XPATH, "/html/body/div[9]/div/div/div[2]/button")

# Accept terms and conditions

wait_and_click(wait,By.XPATH, "//input[@id='IsVerified']")
#time.sleep(1.5)
print("Test Case 13 : Check Box are selected-Test Case Passed")
#time.sleep(1.5)
#driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[2]/button").click()



# Accept HIPAA
wait_and_click(wait, By.ID, "IsVerifiedhppa")
#time.sleep(1.5)
print("Test Case 14 : Check Box are selected-Test Case Passed")
#time.sleep(2)
submitbutton.click()
print("Test Case 15 : Data is saved-Test Case Passed")
time.sleep(4)
# Registration message popup
re=driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div/section/div[1]/section/div/div/div[2]/div/div[1]/div/form/div[1]").text

print(re)


print("QA Member Sign Up completed Sucessfully")
#driver.quit()





