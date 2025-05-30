import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    # start_urls = ["https://www.audible.com/search"]

    # define max pages limit
    max_pages = 5  # change this to set the number of pages to scrape
    page_count = 1  # counter for tracking pages

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.audible.com/search',
            callback=self.parse,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
                     },
        )

    def parse(self, response):
        product_container = response.xpath(
            '//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for product in product_container:
            book_title = product.xpath(
                './/h3[contains(@class, "bc-heading")]/a/text()').get()
            book_author = product.xpath(
                './/li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath(
                './/li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                'title': book_title,
                'author': book_author,
                'length': book_length,
                'User-Agent': response.request.headers['User-Agent'],
            }

        # stop crawling if max pages is reached
        if self.page_count >= self.max_pages:
            return

        pagination = response.xpath(
            '//ul[contains(@class, "pagingElements")]')
        next_page_url = pagination.xpath(
            './/span[contains(@class, "nextButton")]/a/@href').get()
        button_disabled = pagination.xpath(
            './/span[contains(@class , "nextButton")]/a/@aria-disabled').get()

        if next_page_url and button_disabled == None:
            self.page_count += 1  # increment page counter
            yield response.follow(
                url=next_page_url,
                callback=self.parse,
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
                         },
            )
