from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the Chrome WebDriver executable
driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver.get("https://www.lightnovelworld.com/account/logintypes") 

# Use find_element_by_link_text to locate the Google login link by its text
google_login_link = driver.find_element(By.LINK_TEXT,"LOG IN WITH GOOGLE")
google_login_link.click()


#driver.quit()
