# ==== clicking on a button ====

# == when locating an element, especially xpath, use command+f (find). then type out the path to verify it is correct. if so it will be highlighted and will show a 1 of 1 match ==
# = remember, when using an xpath you must use single and double quotes or python will think the code is done at the first set of quotes

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# import By
from selenium.webdriver.common.by import By
import time


website = 'https://www.adamchoi.co.uk/overs/detailed'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)

# locate the button
# # find_element(By.XPATH, "xpath")
all_matches_button = driver.find_element(
    By.XPATH, '//label[@analytics-event="All matches"]')
# click on the button
all_matches_button.click()


# = methods to keep the browser oen before closing it =

# 1. using an input - This keeps the script running until you manually close the browser.
input("Press Enter to close the browser...")  # Keeps the browser open
driver.quit()  # Closes the browser properly when you press Enter (press enter in the terminal)

# 2. use time.sleep() - This pauses execution for a set time before closing the browser.
# import time

# use time.sleep(10)  # Keeps the browser open for 10 seconds
# driver.quit()

# 3. Use driver.implicitly_wait() - This ensures the browser waits for elements before timing out.
# driver.implicitly_wait(10)  # Waits up to 10 seconds for elements

# 4. Run in Interactive Mode - If running from a script, you can add:
# import code
# code.interact(local=locals())  # Opens an interactive console, keeping the browser open
