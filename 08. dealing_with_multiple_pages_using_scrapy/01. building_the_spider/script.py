# ==== building the spider ====

# 1. new project folder:
# in terminal
# scrapy startproject audible_spider

# 2.
# cd to new project folder

# 3. create the spider:
# in the terminal type:
# scrapy genspider audible www.audible.com/search

# 4. locate the xpath for the element
# //div[@class="adbl-impression-container "]

# 5. find the container for each item
# //div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]

# 6. create the product container variable

# 7. create the for loop to loop through the title, author, and length

# 8. find the xpath for the title, author, and length (runtime):

# 9. yield the title, author, and runtime

# 10. open the terminal to extract the data:
# scrapy crawl audible

# 11. once we know the data extraction ws good we store it in a file (csv, json)
# scrapy crawl audible -o audible_one_page.csv
