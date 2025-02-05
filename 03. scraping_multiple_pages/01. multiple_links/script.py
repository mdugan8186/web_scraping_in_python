# ==== scraping multiple links within the same page ====

from bs4 import BeautifulSoup
import requests
import time
import random

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
# add time here to prevent overwhelming the server and being blocked
time.sleep(random.uniform(2, 5))
content = result.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])


# print(title)
# print(links)

# by adding list slicing after links you can go through a certain number of links. or even start at a certain number and end at certain number
for link in links[:2]:
    website = f'{root}/{link}'
    result = requests.get(website)
    # prevents rate limiting
    time.sleep(random.uniform(2, 5))
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find(
        'div', class_='full-script').get_text(strip=True, separator=' ')

    print(title)
    # print(transcript)

    with open(f'{title}.text', 'w') as file:
        file.write(transcript)
