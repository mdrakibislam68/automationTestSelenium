import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(
    filename='signup.txt',  # Log file name
    level=logging.INFO,           # Set the log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Initialize the WebDriver
logging.info("Starting the WebDriver session...")

# Initialize the WebDriver
try:
    driver = webdriver.Chrome()  # Ensure the correct WebDriver is installed
    logging.info("WebDriver initialized successfully.")

    # Open the webpage
    driver.get('https://www.agoda.com/')
    logging.info("Navigated to Agoda website.")

    # Create a WebDriverWait object
    wait = WebDriverWait(driver, 10)

    # Wait for the "Create account" button to be clickable and click it
    button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-element-name='sign-up-button' and contains(., 'Create account')]")
    ))

    button.click()
    logging.info("Clicked on the 'Create account' button successfully.")

except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")

finally:
    # Ensure WebDriver session is closed
    if 'driver' in locals():
        # driver.quit()
        logging.info("WebDriver session closed.")