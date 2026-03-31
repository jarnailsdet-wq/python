#
import os
import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def update_profile_and_upload_image():
    image_name = "profile_picture.jpg"  # Replace with your image file name
    image_path = os.path.join(os.getcwd(), image_name)
    
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        with open(image_path, 'wb') as f:
            f.write(b'\xFF\xD8\xFF\xE0' + b'\x00\x10' + b'JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00' + b'\xFF\xD9')
        print(f"Dummy image file created: {image_path}")
    else:
        print(f"Image file already exists: {image_path}")
            
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        print("Navigating to the Lemniiska Qa...")
        driver.get("http://qa.lemniska.com/")            
        time.sleep(3)
        print("Loggin In...")
        driver.find_element(By.XPATH, "/////////////////").click()
        driver.find_element(By.XPATH, "/////////////////").click()
    
    
    print("uploading profile picture...")
    file_input = driver.find_element(By.XPATH, '//*[@id="UserPictureId"]')
    file_input.send_keys(image_path)
    time.sleep(3)
        
if __name__ == "__main__":
    update_profile_and_upload_image()