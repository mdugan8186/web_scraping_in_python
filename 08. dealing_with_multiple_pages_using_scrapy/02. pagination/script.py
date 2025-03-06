# ==== pagination ====

# 1. use inspect to locate the pages, then build an xpath:
# //ul[contains(@class, "pagingElements")]

# 2. crate the pagination variable

# 3. inspect the next page button and build an xpath:
# //span[contains(@class, "nextButton")]

# 4. create the next_page variable

# 5. write a condition for the next page. if there is a next page or if the next page exists, go to it, but if theres isn't a next page stop the scraping process

# 6. extract data:
# scrapy crawl audible

# 7. save extracted data (csv, json):
# scrapy crawl audible -o multiple_pages.csv
