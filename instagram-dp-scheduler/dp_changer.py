from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, json
import os

# Load schedule data
with open('schedule.json', 'r') as f:
    data = json.load(f)

username = data['username']
password = data['password']

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=options)

# Open Instagram Login
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

# Login
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
time.sleep(10)

# Navigate to profile edit page
try:
    driver.get('https://www.instagram.com/accounts/edit/')
    time.sleep(5)
    
    print("\n✅ You are now on the Instagram profile edit page.")
    print("👉 Please manually upload the DP from here.")
    print("📷 Image path (reference):", data['image_path'])
    print("🕓 Schedule time:", data['time'])

    # Optional: Keep window open for manual action
    input("Press Enter after you've updated the DP...")

except Exception as e:
    print("❌ Error navigating:", e)

driver.quit()
