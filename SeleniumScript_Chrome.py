from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Define the ChromeDriver service
service = Service('/usr/local/bin/chromedriver')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Example usage
driver.get('https://www.google.com')
print(driver.title)
driver.quit()
