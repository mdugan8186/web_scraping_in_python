# ==== scrapy templates and how to find elements with scrapy ====

# == there are two popular templates ==

# 1. scrapy.Spider - this is the simplest spider and will be used more ofter in the course. it doesn't provide any special functionality but we can customize this template to scrap the way we want

# 2. CrawlSpider - this is the most commonly used spider for crawling regular websites. it provides some mechanisms for following links by defining a set of rules. note that crawling is not the same as scraping a website. a crawler usually browses the world wide web for the purpose of web indexing, but web scraping is more about extracting information from websites. a crawl spider might not be the best suited for your web scraping project


# == finding elements with scrapy ==

# we use response to find elements with scrapy, just like the driver in selenium or the soup in beautifulsoup. the response represents the response we get after we send requests to a website.
# unlike selenium we can only find elements with Xpath on scrapy. scrapy doesn't have functions like find_element

# to use Xpath in scrapy
# response.xpath('//tag[@attributeName="Value"]')

# get a single element
# response.xpath().get()

# get all elements (returns a list)
# response.xpath().getall()


# == yield ==

# we will be using the yield keyword a lot. it works the same way the return keyword works when you define a function. however the yield keyword returns values from a function without destroying the states of it's local variable
