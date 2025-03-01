import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()

        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

        # add a callback of parse_country
        # this callback will call the parse_country every time it goes to a new link
        # add the meta tag to use this later in the code for the country name
            yield response.follow(url=link, callback=self.parse_country, meta={'country': country_name})

    def parse_country(self, response):
        # add the country name variable that we made fromm the meta tag
        country = response.request.meta['country']

        # we can keep the xpath long or shorten it up
        # long - original xpath
        # rows = response.xpath('(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr')
        # short - new xpath that has contains
        rows = response.xpath(
            "(//table[contains(@class, 'table')])[1]/tbody/tr")

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                # add the country variable
                'country': country,
                'year': year,
                'population': population,
            }
