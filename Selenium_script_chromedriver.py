import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Create a new instance of the Chrome driver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")  # Required for some environments (e.g., CI)
options.add_argument("--disable-dev-shm-usage")  # Required for some environments (

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Navigate to a website
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# Find an element using relative XPath
element = driver.find_element(By.XPATH,"//input[@type='text']")
# Perform actions on the element
element.send_keys('Sagandeep')
print(element.text)
links=driver.find_elements(By.TAG_NAME,'a')

print(len(links))
for link in links:
    print(link.get_attribute('href'))

# Close the browser
driver.quit()
