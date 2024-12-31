# textInput
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


logging.basicConfig(
    filename='search.txt',  # Log file name
    level=logging.INFO,           # Set the log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Initialize the WebDriver
logging.info("Starting the WebDriver session...")

# Initialize the WebDriver
try:
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure the correct WebDriver is installed
    logging.info("WebDriver initialized successfully.")

    # Open the webpage
    driver.get('https://www.agoda.com/')
    logging.info("Navigated to Agoda website.")

    # Create a WebDriverWait object
    wait = WebDriverWait(driver, 30)  # Set the timeout to 30 seconds

    # Wait for the input field to be clickable and activate it
    # input_button = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//button[@aria-label='Enter a destination or property']")
    # ))
    # input_button.click()
    logging.info("Clicked on the search button to activate the input field.")

    # Wait for the actual input field to appear
    actual_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@aria-label='Enter a destination or property']")
    ))

    # Clear the input field (optional but recommended)
    actual_input.clear()

    # Enter the search value "Bogura"
    actual_input.send_keys("Bogura")
    logging.info("Entered the search term 'Bogura' successfully.")

    searchButton = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-element-name='search-button']")
    ))
    # time.sleep(1)
    searchButton.click()
    logging.info("search button clicked")
    logging.info("Waiting for 30 seconds to allow observation of the results.")
    time.sleep(10)
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")

# finally:
#     # Ensure WebDriver session is closed
#     if 'driver' in locals():
#         logging.info("WebDriver session closed.")