# ==== exporting data to a csv file with pandas ====

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# Setup WebDriver
website = 'https://www.adamchoi.co.uk/overs/detailed'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)

# Wait for the "All matches" button to be clickable and click it
try:
    all_matches_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//label[@analytics-event="All matches"]'))
    )
    all_matches_button.click()
except Exception as e:
    print(f'Failed to find "All matches" button: {e}')
    driver.quit()
    exit()

# Wait for the table to be visible
try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//table'))  # Make sure table exists
    )
except Exception as e:
    print(f'Failed to find match table: {e}')
    driver.quit()
    exit()

# Now get all rows from the table
matches = table.find_elements(By.TAG_NAME, 'tr')

# Extract data
date = []
home_team = []
score = []
away_team = []

for match in matches:
    try:
        # Check if the row contains `<td>` elements (not a header row)
        cells = match.find_elements(By.TAG_NAME, "td")
        if len(cells) < 4:  # Skip rows with less than 4 cells
            continue

        date.append(cells[0].text)
        home_team.append(cells[2].text)
        score.append(cells[3].text)
        away_team.append(cells[4].text)

        # print(cells[0].text, cells[2].text, cells[3].text, cells[4].text)

    except Exception as e:
        print(f'Skipping row due to missing elements: {e}')

# Quit the browser
driver.quit()

# creating a data frame
df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
})

df.to_csv('football_data.csv', index=False)
print(df)
