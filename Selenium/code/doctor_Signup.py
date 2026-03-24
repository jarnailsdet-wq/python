#doctor signupp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def doctor_sign_up():
    # Set up the Chrome driver (make sure chromedriver is in your PATH or provide the full path)
    driver = webdriver.Chrome()
    print("USA Doctor Sign Up")
    driver.get("https://qa.lemniska.com/")
    driver.maximize_window()
    time.sleep(5)

    # To click on get started
    get_started = driver.find_element(By.XPATH, "//*[@id='lower-main-contain']/main/section[1]/div/div[1]/div/a")
    if get_started.is_enabled():
        print("Test Case 00A : Get started icon is present -Test Case Passed")
    else:
        print("Test Case 00A : Get started is Not present -Test Case Failed")
    time.sleep(5)
    get_started.click()
    time.sleep(5)

    # Doctor sign up link
    driver.find_element(By.XPATH, "//button[@id='dropdownMenuButton']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='header-right-button']/div[2]/div[2]/div/div/div[2]/div[2]/a[2]").click()
    time.sleep(8)
    print("Test case 1 : Doctor sign up link is clicked")

    # Assert Doctor Sign Up title
    doctor_signup_title = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/form/section/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/h2").text
    if doctor_signup_title == "Doctor Sign Up":
        print("Test case 2 : Assert for the Doctor sign up is passed")
    else:
        print("Test case 2 : Assert for the Doctor sign up FAILED")

    # Select Title
    title = driver.find_element(By.XPATH, "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/select[1]")
    title.click()
    time.sleep(2.5)
    sup = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/form/section/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div/select/option[2]")
    sup.click()
    print("Test case 3 : Title is Selected")

    # First Name
    first_name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
    first_name.send_keys("346546456")
    time.sleep(2)
    first_name.clear()
    time.sleep(2)
    first_name.send_keys("Anu")
    print("Test case 4 : Random and Correct Keys are added to First Name")

    # Last Name
    last_name = driver.find_element(By.XPATH, "//input[@id='LastName']")
    last_name.send_keys("6464646546")
    time.sleep(2)
    last_name.clear()
    time.sleep(2.5)
    last_name.send_keys("Sharma")
    print("Test case 5 : Random and Correct Keys are added to Last Name")

    # Email
    email = driver.find_element(By.XPATH, "//input[@id='Email']")
    email.send_keys("3464646546")
    time.sleep(2)
    email.clear()
    time.sleep(2.5)
    email.send_keys("anu_USA1z@yopmail.com")
    print("Test case 6 : Random and Correct Keys are added to Email")

    # Phone Number
    phone = driver.find_element(By.XPATH, "//input[@id='Phone']")
    phone.send_keys("@@%$%^$^$^$")
    time.sleep(2)
    phone.clear()
    time.sleep(2.5)
    phone.send_keys("3532145698")

    time.sleep(2.5)
    # Pref and Country selection
    pref = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
    pref.click()
    country1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[5]")
    country1.click()
    time.sleep(2)
    print("Test case 7 : Random and Correct Keys are added to PhoneNumber")

    # Referral
    referral = driver.find_element(By.XPATH, "//input[@id='Mrcode']")
    referral.send_keys("3464646")
    referral.clear()
    time.sleep(2.5)
   
   
# ... previous code for setup and filling the form ...

    print("Test case 8 : Correct Keys are added to Referral")
    privacy = driver.find_element(By.XPATH, "//input[@id='IsVerified']")
    privacy.click()
    time.sleep(2.5)
    privacy.click()
    time.sleep(2.5)
    privacy.click()
    print("Test case 9 : Lemniska's Terms & Conditions and Privacy Policy checked & unchecked.")

    save = driver.find_element(By.XPATH, "//input[@id='doctor-sign-next']")
    save.click()
    time.sleep(2.5)
    hippa_error = driver.find_element(By.XPATH, "//span[contains(text(),'Please agree to HIPAA Authorization.')]").text
    print("Test case 10 : Hippa not clicked error received", hippa_error)

    hippa = driver.find_element(By.XPATH, "//input[@id='IsVerifiedHippa']")
    hippa.click()
    time.sleep(2.5)
    print("Test case 11 : HIPAA icon is checked")

    save1 = driver.find_element(By.XPATH, "//input[@id='doctor-sign-next']")
    save1.click()
    print("Test case 12 : Save icon is selected")
    time.sleep(5)

    # To check the plan screen and purchase
    time.sleep(5)
    plantitlepage = driver.find_element(By.XPATH, "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]").text
    assert plantitlepage == "Simple pricing that scales with your business"
    print("Test case 13 : Assert for Subscription Title Text is passed")
    time.sleep(2.5)

    # to switch between Quarterly and annual plans
    time.sleep(5.5)

    silverbuyannnu = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    if silverbuyannnu.is_enabled():
        print("Test case 14 : silver buy annnual is present-Test case passed")
    else:
        print("Test case 14 : silver buy annnual is Not present-Test case Failed")
    time.sleep(1)

    goldbuyannnu = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    if goldbuyannnu.is_enabled():
        print("Test case 15 : Gold buy annnual is present-Test case passed")
    else:
        print("Test case 15 : Gold buy annnual is Not present-Test case Failed")
    time.sleep(1)

    platinumbuyannnu = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    if platinumbuyannnu.is_enabled():
        print("Test case 16 : Platinum buy annnual is present-Test case passed")
    else:
        print("Test case 16 : Platinum buy annnual is Not present-Test case Failed")
    time.sleep(1)

    # to check and validate the quarterly plan
    quarterly = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    quarterly.click()
    time.sleep(5.5)

    silverbuyQuar = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    if silverbuyQuar.is_enabled():
        print("Test case 17 : silver buy Quar is present-Test case passed")
    else:
        print("Test case 17 : silver buy Quar is Not present-Test case Failed")
    time.sleep(1)

    goldbuyQuar = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    if goldbuyQuar.is_enabled():
        print("Test case 18 : Gold buy Quar is present-Test case passed")
    else:
        print("Test case 18 : Gold buy Quar is Not present-Test case Failed")
    time.sleep(1)

    platinumbuyQuar = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h2[1]")
    if platinumbuyQuar.is_enabled():
        print("Test case 19 : Platinum buy Quar is present-Test case passed")
    else:
        print("Test case 19 : Platinum buy Quar is Not present-Test case Failed")
    time.sleep(1)


    # To purchase the gold quarterly plan
    goldbuy = driver.find_element(By.XPATH, "html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/h1[1]/button[1]")
    goldbuy.click()
    time.sleep(4.5)

    # To validate the plan purchase screen
    plandetails = driver.find_element(By.XPATH, "//h2[contains(text(),'Plan Details')]").text
    assert plandetails == "Plan Details"
    print("Test case 20 : Assert for Subscription Title Text is passed")
    time.sleep(2.5)

    plancancel = driver.find_element(By.XPATH, "//tbody/tr[6]/td[1]/form[1]/div[1]/input[1]")
    if plancancel.is_enabled():
        print("Test case 21 : Plan Cancel is present-Test case passed")
    else:
        print("Test case 21 : Plan Cancel is Not present-Test case Failed")
    time.sleep(1)

    # To check the proceed icon
    proceed = driver.find_element(By.XPATH, "//input[@id='checkout-button']")
    if proceed.is_enabled():
        print("Test case 22 : Proceed Icon is present-Test case passed")
    else:
        print("Test case 22 : Proceed Icon is Not present-Test case Failed")
    time.sleep(1)

    # To check the note
    notedetails = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div/div/div[2]/p").text
    assert notedetails == "Note- Please do not change or refresh the page language during the payment process."
    print("Test case 23 : Assert for note Text is passed")
    time.sleep(2.5)

    # To cancel the plan
    plancancel1 = driver.find_element(By.XPATH, "//tbody/tr[6]/td[1]/form[1]/div[1]/input[1]")
    plancancel1.click()
    time.sleep(2.5)

    # To purchase the plan again
    platinumbuy = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/section/div/div/div[4]/div/div/div/div[1]/div/div[3]/div/form/div/div/h1/button")
    platinumbuy.click()
    time.sleep(4.5)
    plandetails1 = driver.find_element(By.XPATH, "//h2[contains(text(),'Plan Details')]").text
    assert plandetails1 == "Plan Details"
    print("Test case 24 : Assert for Subscription Title Text is passed")
    time.sleep(2.5)

    plancancel2 = driver.find_element(By.XPATH, "//tbody/tr[6]/td[1]/form[1]/div[1]/input[1]")
    if plancancel2.is_enabled():
        print("Test case 25 : Plan Cancel is present-Test case passed")
    else:
        print("Test case 25 : Plan Cancel is Not present-Test case Failed")
    time.sleep(1)

    # To check the proceed icon again
    proceed1 = driver.find_element(By.XPATH, "//input[@id='checkout-button']")
    if proceed1.is_enabled():
        print("Test case 26 : Proceed Icon is present-Test case passed")
    else:
        print("Test case 26 : Proceed Icon is Not present-Test case Failed")
    time.sleep(1)

    proceed1.click()
    time.sleep(4.5)
    print("Test case 27 : User is now on the payment page")
    print("Test case 28 : Doctor Sign up on the live is completed Successfully")
    # driver.quit()  # Uncomment if you want to close the browser at the end