import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(
    filename='logout.txt',  # Log file name
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

    # Create a WebDriverWait object for waiting
    wait = WebDriverWait(driver, 10)

    # Wait for the user avatar button to be clickable and click it
    avatar_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-element-name='user-avatar']")
    ))
    avatar_button.click()
    logging.info("Clicked on the 'User Avatar' button successfully to show sign-out options.")

    # Wait for the 'SIGN OUT' button to be clickable and click it
    sign_out_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-element-name='sign-out-btn' and contains(., 'SIGN OUT')]")
    ))
    sign_out_button.click()
    logging.info("Clicked on the 'SIGN OUT' button successfully.")

except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")

finally:
    # Ensure WebDriver session is closed
    if 'driver' in locals():
        driver.quit()
        logging.info("WebDriver session closed.")