import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Setup and Teardown for the browser."""
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    # driver.quit() # Uncomment to close browser after test


@pytest.mark.parametrize("session", ["USA", "India", "UK"])
def test_member_signup_navigation(driver, session):
    wait = WebDriverWait(driver, 10)

    # server += 1

    # Step 1: Navigate
    driver.get("http://qa.lemniska.com/")
    
    # Step 2: Dropdown click
    dropdown_signup = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    dropdown_signup.click()
    
    # Step 3: Click Sign Up
    driver.find_element(By.LINK_TEXT, "Sign up").click()
    
    # Step 4: Assertions
    assert driver.current_url == "http://qa.lemniska.com/membership"
    
    title = driver.find_element(By.XPATH, "//h2[normalize-space()='Member Sign Up']").text
    assert title == "Member Sign Up"