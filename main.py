import os  # OS interaction
from selenium import webdriver  # Browser automation
from selenium.webdriver.common.by import By  # DOM element locators
from selenium.webdriver.chrome.service import Service  # Manages ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait  # Wait for conditions
from selenium.webdriver.support import expected_conditions as EC  # Predefined wait conditions
from selenium.webdriver.chrome.options import Options  # Configure Chrome options
import time  # Time utilities
import subprocess  # Run external commands

def keep_awake():
    """Prevents the system from sleeping."""
    return subprocess.Popen(["caffeinate", "-i"])

def login_to_gmail(email, password):
    chromedriver_path = "/usr/local/bin/chromedriver"  # ChromeDriver path

    # Browser options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without GUI
    chrome_options.add_argument("--disable-notifications")  # Disable pop-ups
    chrome_options.add_argument("--mute-audio")  # Mute audio

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)
    driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube")  # Open Gmail login page

    try:
        # Enter email
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "identifierId"))
        )
        email_field.send_keys(email)
        driver.find_element(By.ID, "identifierNext").click()  # Click "Next"
        time.sleep(2)

        # Enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "Passwd"))
        )
        password_field.send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()  # Click "Next"
        time.sleep(5)

        print("Login successful!")
        return driver
    except Exception as e:
        print(f"Login error: {e}")
        driver.quit()
        return None

def subscribe_to_channel(driver, channel_url):
    """Subscribes to a YouTube channel."""
    try:
        driver.get(channel_url)
        subscribe_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Subscribe')]"))
        )
        button_text = subscribe_button.text.strip().lower()
        if "subscribe" in button_text:
            subscribe_button.click()
            print("Subscribed!")
        elif "subscribed" in button_text:
            print("Already subscribed.")
        else:
            print("Unexpected button state.")
    except Exception as e:
        print(f"Subscription error: {e}")

def login_and_subscribe_to_channels(email, password, file_path):
    """Logs in and subscribes to channels from a file."""
    try:
        with open(file_path, 'r') as file:
            channels = [channel.strip() for channel in file.readlines()]
            print(f"Loaded {len(channels)} channels.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    driver = login_to_gmail(email, password)  # Login
    if driver:
        for channel_url in channels:
            subscribe_to_channel(driver, channel_url)  # Subscribe
        input("Press Enter to close the browser...")
        driver.quit()

# Public placeholder credentials and file path
gmail_email = 'your_email@gmail.com'  # Replace with your email
gmail_password = 'your_password'  # Replace with your password
file_path = 'path_to_your_channel_list.txt'  # Replace with your file path

if __name__ == "__main__":
    caffeinate_process = keep_awake()  # Prevent system sleep
    try:
        login_and_subscribe_to_channels(gmail_email, gmail_password, file_path)
    finally:
        caffeinate_process.terminate()  # Stop caffeinate
