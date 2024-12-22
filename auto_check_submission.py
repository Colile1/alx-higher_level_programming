#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_all_check_buttons():
    # Initialize Chrome driver
    driver = webdriver.Chrome()
    
    # Replace with your target website URL
    url = "https://intranet.alxswe.com/projects/303"
    driver.get(url)
    
    # Wait for page to load and find all check submission buttons
    # Adjust the selector based on the actual button class/id/text
    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.check-submission-btn"))
    )
    
    # Click each button with a small delay
    for button in buttons:
        button.click()
        time.sleep(2)  # Adjust delay as needed
    
    # Keep browser open for a while to see results
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    click_all_check_buttons()
