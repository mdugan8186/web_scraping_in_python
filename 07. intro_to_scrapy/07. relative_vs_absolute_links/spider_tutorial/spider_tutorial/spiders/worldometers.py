import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()

        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            # == absolute ==
            # 1 & 2 will be turning the relative links into absolute links

            # 1. the get the rest of the link we make an f string and concatenate the beginning of the webpage link to the the rest of the link we scraped
            # this work around is not the ideal way to handle this
            # absolute_url = f'https://www.worldometers.info/{link}'

            # 2. this is a better way to handle this is to use urljoin()
            # absolute_url = response.urljoin(link)

            # == relative ==
            # 3. use the response.follow(). this doesn't convert anything and just uses the relative link

            # == working with absolute (1 or 2) ==
            # yield scrapy.Request(url=absolute_url)

            # == working with relative (3) ==
            yield response.follow(url=link)
