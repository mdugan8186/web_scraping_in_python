# ==== scraping APIs - dealing with pagination ====

# with infinite scrolling as you scroll down more pages will load in the network/ XHR/ preview tab

# with this page scroll down until no pages load and you see the limit. in this case it will be 10 because once you click on page 10 has_next is set to False


# == handling pagination ==
# 1. create a variable called has_next:
# create this is the parse function under the yield
# has_next = json_response.get('has_next')

# 2. write a conditional statement:
# a. if has_next - this means if has_next = True

# b. create a variable to represent the page:
# next_page_number = json_response.get('page') + 1
# this will help us scrap all the pages

# c. make a yield statement:
# this will go to the next page the variable is set to True

# d. create a variable with an f string to help concatenate the url with the next page:
# url=f'https://quotes.toscrape.com/api/quotes?page={next_page_number}'
# get the url from the start_urls and use the next_page_number variable to replace the 1

# e. add a second argument, the callback:
# url = f'https://quotes.toscrape.com/api/quotes?page={next_page_number}',
# callback = self.parse


# == run the script ==
# scrapy crawl quotes


# == save the data in a json or csv file ==
# scrapy crawl quotes -o quotes_pagination.json
