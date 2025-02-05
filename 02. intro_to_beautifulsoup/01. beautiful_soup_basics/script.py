# ==== beautifulsoup basics ====

# imports
from bs4 import BeautifulSoup
import requests

# 1. fetching the page (obtain a response object)
result = requests.get('www.google.com')

# 2. page content
content = result.text

# 3. create soup
soup = BeautifulSoup(content, 'lxml')


# locating an element by the ID
# soup.find(id='specific_id')

# locate an element by class
soup.find('tag', class_='class_name')

# == example page ==
# <article class='main-article'>
#     <h1> Titanic (1997) </h1>
#     <p> class='plot'> 84 years later... </p>
#     <div class='full-script'> 12 meters. </div>
# </article>


# to locate the article element by its class name
soup.find('article', class_='main-article')

# to locate the h1 element
soup.find('h1')

# to locate multiple elements
soup.find_all('h2')


# .find() returns an element
# .find_all() returns a list
