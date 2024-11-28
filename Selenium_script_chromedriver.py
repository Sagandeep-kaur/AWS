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
#from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver

"""
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path = r'C:/Users/sagandeepk/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(, service= service, options=options)

chrome_install = ChromeDriverManager().install()
folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")
service = webdriver.ChromeService(chromedriver_path)
"""
#chrome_options = Options()
#chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(options=chrome_options)


#driver = webdriver.Chrome(service = service, options = options)

# Navigate to a website
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# Find an element using relative XPath
element = driver.find_element(By.XPATH,"//input[@type='text']")
# Perform actions on the element
element.send_keys('Sagandeep')
# Close the browser
driver.quit()
