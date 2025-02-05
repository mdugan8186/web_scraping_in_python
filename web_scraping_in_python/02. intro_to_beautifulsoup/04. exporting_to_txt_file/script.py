# ==== Exporting data to a TXT file ====

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338#google_vignette'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

transcript = box.find(
    'div', class_='full-script').get_text(strip=True, separator=' ')

# print(title)
# print(transcript)

# to create a file in python
with open(f'{title}.txt', 'w') as file:
    file.write(transcript)

# remember this will crete and write the file in the present working directory
