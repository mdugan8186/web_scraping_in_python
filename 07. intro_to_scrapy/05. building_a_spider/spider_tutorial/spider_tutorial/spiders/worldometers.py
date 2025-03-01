import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country"]

    # every time we want to locate an element we will use the response variable
    # we will make variables for the elements we looked up in the shell video
    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a/text()').getall()

        # to display the data in a dictionary we'll use the yield keyword
        yield {
            'title': title,
            'countries': countries,
        }


# 1. open the terminal. to make this work you MUST be located in the folder with scrapy.cfg file. the name of this folder is the same name as the project you created it for

# 2. write the command:
# scrapy crawl name_of_spider

# in this case
# scrapy crawl worldometers
