# ==== scraping APIs - building the spider ====

# when scraping an API we'll be working with a json file and parse it in python

# to add infinite scrolling to the website add /scroll after the .com

# == inspecting the page ==
# 1. when inspecting the website with dev tools we'll use the networks tab instead of the elements tab

# 2. click on the XHR tab:

# 3. refresh the page:

# 4. click on the new item that popped up:
# a. look at the request url: - it has the webpage but with the added text for the API

# b. click on preview - here is a json object:
# check the elements
# - has_next is set to True
# - quotes has all the quotes listed in the website


# == start a new project ==
# scrapy startproject api_project


# == create a spider ==
# 1. scrapy genspider quotes quotes.toscrape.com

# 2. go back to the webpage and copy the link from the header request url:
# https://quotes.toscrape.com/api/quotes?page=1

# 3. open the spiders file and paste the link in the start_urls

# 4. in the parse function:
# to see how the code looks print(response.body)

# 5. run the spider in the terminal:
# scrapy crawl quotes


# == convert the json file into a dictionary ==
# 1. import json

# 2. remove the print statement and create a new variable:
# json_response = json.loads(response.body)

# 3. get the quotes key:
# we got the quotes key from the preview in the networks tab
# quotes = json.get('quotes')

# 4. view the data:
# print(quotes)
# after it prints you can view the keys


# == look through the elements inside quotes ==
# 1. replace the print statement with a for loop:
# for quote in quotes:
#             yield {
#                 'author': ,
#                 'tags': ,
#                 'quotes': ,
#             }

# 2. go back to the browser:

# 3. check the keys one more time in the preview tab:
# we see the author, tags, and text keys
# - the author has the link, name, and slug

# 4. author:
# 'author': quote.get('author').get('name'),

# 5. tags:
# 'tags': quote.get('tags'),

# 6. quotes:
# 'quotes': quote.get('text'),


# == test the code ==
# 1. in the terminal:
# scrapy crawl quotes


# == check the data in a more readable format ==
# 1. make a json or csv file:
# scrapy crawl quotes -o quotes.json
