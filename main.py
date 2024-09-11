from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import os

def auto_login(u, p, url):
    path = "C:/Users/Manan Sethi/OneDrive/Desktop/chapter 1/login autobot/chromedriver-win64/chromedriver.exe"
    
    # Check if the ChromeDriver path is a valid file
    if not os.path.isfile(path):
        raise ValueError(f"The path is not a valid file: {path}")
    
    # Initialize the Chrome WebDriver with the specified path
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open a website
        driver.get(url)

        # Find the username field and input the username
        driver.find_element(By.ID, "username").send_keys(u)
        
        # Find the password field and input the password
        driver.find_element(By.ID, "password").send_keys(p)
        
        # Find the login button and click it
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign in']").click()

        # Optional: Add a delay or wait for user input
        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser
        driver.quit()

username = input("Enter your username: ")
password = input("Enter your password: ")
url = "https://www.linkedin.com/login"
auto_login(username, password, url)
