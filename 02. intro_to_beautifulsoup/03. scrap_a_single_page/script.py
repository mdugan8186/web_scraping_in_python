# ==== how to scrap a single page ====

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338#google_vignette'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


# == get the title ==

# this will get the everything in the article tag
box = soup.find('article', class_='main-article')

# to get the title we can do this
title_1 = soup.find('h1').get_text()
# or
# we can use box to exclude everything that isn't in the box
title_2 = box.find('h1').get_text()

print(title_2)


# == get the transcript ==

transcript = box.find(
    'div', class_='full-script').get_text(strip=True, separator=' ')

print(transcript)


# to avoid a text without any spaces in it when we view the data in another format (excel, or a data frame) we have to add parameters to the .get_text()
# strip=True
# separator=' '


# when finding elements it is recommended to find elements un this order
# 1. ID (#id) – Most specific and fastest.
# 2. Class (.class) – Can be shared among multiple elements.
# 3. Tag Name (<tag>) – Use when ID and class aren’t unique enough.
# 4. CSS Selectors (soup.select()) – Useful for complex structures.
# 5. Attributes (attrs={"attribute": "value"}) – When elements have unique attributes like data-*, href, etc.
# 6. Text Content (text) – When targeting elements by visible text.
# 7. XPath (lxml or html.parser with select() or find_all()) – Use as a last resort when elements are deeply nested or dynamically generated.
