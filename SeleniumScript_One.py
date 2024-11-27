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
element = driver.find_element(By.XPATH,"//input[@type='text']")
# Perform actions on the element
element.send_keys('Sagandeep')
# Close the browser
driver.quit()
"""
# chaining xpaths
#//form[contains(@class,'form')]//following::div//input[@id='userpassword']

# implicit wait syntax
driver.implicitly_wait(10)

# explicit wait syntax
wait = WebDriverWait(driver, 600)
# fluent wait
wait = WebDriverWait(driver, timeout=600, poll_frequency=0.5)
wait.until(EC.element_to_be_clickable(By.XPATH, 'cddc'),
               "Complete Task Button is disabled").click()
wait.until(EC.visibility_of_element_located(By.XPATH,'Alert'),
               "Alert is not visible")

# action class

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

# context click the item
actions.context_click(on_element = element)
# drag and drop the item
actions.drag_and_drop(source_element, target_element)
actions.double_click(on_element = element)
actions.perform()

# perform the operation
actions.move_to_element(element).click().perform()

# use enumerate in python when you want to access both index and value of each item in the iterable

my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(index, value)

drop=Select(driver.find_element_by_id(‘ ‘))

drop.select_by_visible_text(” “)
drop.select_by_index(0)
drop.select_by_value(" ")

#get selected item with method first_selected_option
o= drop.first_selected_option
a = drop.all_selected_options

dropdown = Select(driver.find_element(By.ID,"lang2"))
for opt in dropdown.options:
    dropdown.select_by_visible_text(opt.get_attribute("innerText"))

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

# one step backward in browser history
driver.back()

# one step backward in browser history
driver.forward()

# switching to 3rd window
driver.switch_to.window(driver.window_handles[2])

# switch to 1st frame
driver.switch_to.frame("packageListFrame")

# back to default web page frame
driver.switch_to.default_content()

"""