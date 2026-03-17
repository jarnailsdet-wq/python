#
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    driver = p.chromium.launch(headless=False)
    page = driver.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    print(page.title())
    page.get_by_text("Form Authentication").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button" ,name="Login").click()
    message = page.locator("#flash").text_content()
    print(f"Massage : {message}")
    page.wait_for_timeout(2000)
    driver.close()
    