# ==== importing libraries and creating the driver ====

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

website = 'https://www.adamchoi.co.uk/overs/detailed'
# if using this code you do not have to define a path since ChromeDriverManager automatically installs and manages ChromeDriver for you. it finds the correct driver and provides the path to Selenium internally
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(website)
print("Page title:", driver.title)

driver.quit()
