import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging to a file
logging.basicConfig(
    filename='selenium_log.txt',  # Log file name
    level=logging.INFO,           # Set the log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://dev-rooftop.boomdevs.com/hackney/#sauna-session-options')

wait = WebDriverWait(driver, 10)
# try:
#     # Wait for all matching buttons
#     buttons = wait.until(EC.presence_of_all_elements_located(
#         (By.XPATH, "//button[contains(text(),'Express Sauna (30 mins)') and @data-service-id='3']")
#     ))

#     # Check if we found any buttons
#     if len(buttons) > 0:
#         # Iterate over the buttons and click them
#         for index, button in enumerate(buttons):
#             button.click()
#             logging.info(f"Clicked button {index + 1} successfully!")
#         print(f"Clicked {len(buttons)} buttons.")
#     else:
#         logging.warning("No buttons found with the specified criteria.")
#         print("No buttons found with the specified criteria.")
        
# except Exception as e:
#     logging.error(f"An error occurred: {e}")
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()
#     logging.info("WebDriver session closed.")

button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Express Sauna (30 mins)') and @data-service-id='3']")))
if len(button) > 0:
    button.click()
else:
    print(f"Button not clicked")
