from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# Create a new instance of the Chrome driver

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', chrome_options=options)

# Navigate to a website
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# Find an element using relative XPath
element = driver.find_element(By.XPATH,"//input[@type='text']")
# Perform actions on the element
element.send_keys('Sagandeep')
# Close the browser
driver.quit()
