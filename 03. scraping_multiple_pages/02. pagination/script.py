# ==== pagination ====

# ==== scraping multiple links within the same page ====

from bs4 import BeautifulSoup
import requests
import time
import random

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
time.sleep(random.uniform(2, 5))
content = result.text
soup = BeautifulSoup(content, 'lxml')

# == pagination ==
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

for page in range(1, int(last_page)+1)[:2]:

    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()

    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    # print(title)
    # print(links)

    for link in links[:2]:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            time.sleep(random.uniform(2, 5))
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find(
                'div', class_='full-script').get_text(strip=True, separator=' ')

            # print(title)
            # print(transcript)

            # with open(f'{title}.text', 'w') as file:
            #     file.write(transcript)

        except:
            print('------ Link not working ----')
            print(link)

        # Move sleep to the bottom of the loop
        time.sleep(random.uniform(2, 5))

    # Add sleep here to prevent too many pagination requests
    time.sleep(random.uniform(2, 5))
