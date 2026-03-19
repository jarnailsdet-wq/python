#
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    driver = p.chromium.launch(headless=False)
    page = driver.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    print(page.title())
    page.get_by_text("A/B Testing").click()  #1
    print(page.title())
    page.wait_for_timeout(2000)
    q1=page.locator("#content").text_content()
    print(q1)
    page.go_back()
    print(page.title())
    page.get_by_text("Add/Remove Elements").click()  #2
    print(page.title())
    page.wait_for_timeout(2000)
    page.get_by_role("button",name="Add Element").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button",name="Delete").click()
    
    page.wait_for_timeout(2000)
    page.go_back()
    
    
    
    