# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging


service = Service(r"C:\Users\mdrak\Downloads\chromeDriver\chromedriver-win64\chromedriver.exe")

# Initialize the Chrome WebDriver with the service
driver = webdriver.Chrome(service=service)

# Open the website
# driver.get('https://rooftopsaunas.com')
driver.get('https://dev-rooftop.boomdevs.com/hackney/#sauna-session-options')

# Find the element (ensure correct locator)
# wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
# element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-service-id]")))

# wait = WebDriverWait(driver, 20)
# button_wrapper = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "uagb-button__wrapper")))

# Scroll to the element and click if needed
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_wrapper)

# If the button inside the wrapper is clickable, click it
# wait = WebDriverWait(driver, 10)
# button_wrapper = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "uagb-button__wrapper")))
#
# # Scroll to the element and ensure it's clickable
# driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button_wrapper)
#
# # Find the link or button inside the wrapper and click it
# button = button_wrapper.find_element(By.TAG_NAME, "a")  # Assuming there's a link inside the wrapper
# if button.is_displayed() and button.is_enabled():
#     button.click()
#     print("Button clicked successfully!")
# else:
#     print("Button is not clickable.")
# print("Button clicked successfully!")

# element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-service-id="3"]')))

# Clear the search input field (if needed) and send a search query
# search_input.clear()
# search_input.send_keys("song")  # Replace with the term you want to search
# search_input.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

# print("Search submitted!")
# element.click()
# print("Element clicked!")
# try:
#     # Wait for the element with data-service-id="3" to appear
#     wait = WebDriverWait(driver, 10)
#     link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Express Sauna")))
#
#     # Perform actions on the element (e.g., click)
#     link.click()
#     print("Element clicked!")
# except Exception as e:
#     print(f"An error occurred: {e}")
# # finally:
# #     # driver.quit()
# #     print(f"An error occurred")
#
# print("Script finished. Browser remains open.")
# WebDriverWait(driver, 30)
# try:
    # Wait for the links to be present
logging.basicConfig(
    filename='selenium_log.txt',  # Log file name
    level=logging.INFO,           # Set the log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)
wait = WebDriverWait(driver, 10)

# Locate all elements with the link text "Express Sauna (30 mins)"
buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Express Sauna (30 mins)']")))

if len(buttons) >= 2:
    buttons[1].click()
    print("Second button clicked successfully!")
else:
    print("There are less than two buttons with the specified text.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     driver.quit()