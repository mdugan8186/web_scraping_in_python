import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies_letter-X"]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
    }

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//ul[@class='scripts-list']/li/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(
            restrict_xpaths="(//a[@rel='next'])[1]")),
    )

    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")
        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            # 'transcript': article.xpath("./div[@class='full-script']/div[@class='subtitle-cue']/p[@class='cue-line']/text()").getall(),
            'url': response.url,
        }
