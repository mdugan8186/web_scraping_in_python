# ==== how to get the HTML from a website ====

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338#google_vignette'

result = requests.get(website)

content = result.text

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())
