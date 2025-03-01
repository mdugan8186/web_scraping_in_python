import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()

        # to get the href
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            # remember to indent the yield since it's part of the for loop
            yield {
                'country_name': country_name,
                'link': link,
            }
