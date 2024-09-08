from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the web application's login page
driver.get("https://app.buildersource.com/admin/site/login?")

# Maximize the window
driver.maximize_window()

# Add an implicit wait to handle timing issues
driver.implicitly_wait(10)

# Locate the username and password fields and input data
username_input = driver.find_element(By.ID, "loginform-username")
password_input = driver.find_element(By.ID, "loginform-password")

# Enter the credentials
username_input.send_keys("testcomp08@mailinator.com")
password_input.send_keys("Test@1234")

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Add a delay to see the login result (can be adjusted or removed based on need)
time.sleep(5)

# Check if login was successful by verifying the presence of an element on the home/dashboard page
try:
    # Locate an element on the dashboard or home page to verify login success (modify selector accordingly)
    dashboard_element = driver.find_element(By.CLASS_NAME, "right-inner-wrapper")  # Replace with actual locator
    print("Login successful!")
except:
    print("Login failed!")

# Close the browser
driver.quit()
