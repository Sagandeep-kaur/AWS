from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to a website
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# Find an element using relative XPath
element = driver.find_element(By.XPATH,"//a[contains(text(), 'Contact')]")
element.click()
# Close the browser
driver.quit()
