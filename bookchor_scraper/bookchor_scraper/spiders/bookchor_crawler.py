import scrapy
from bookchor_scraper.items import BookchorScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BookchorCrawlerSpider(CrawlSpider):
    name = "bookchor_crawler"
    allowed_domains = ["www.bookchor.com"]
    start_urls = ["https://www.bookchor.com/category/1"]
    rules = [Rule(LinkExtractor(allow='fiction', deny = 'nonfiction'), callback='parse', follow=True)]

    def parse(self, response):
        items = response.css('div.product-item')

        for item in items:
            starCount = item.css("ul.rateing li::attr(class)")
            link = item.css('a::attr(href)').get()

            yield response.follow(link, callback=self.parser, meta = {'starCount' : starCount})

    def parser(self, response):
        item = BookchorScraperItem()
        starCount = response.meta.get('starCount')

        item['title'] = response.css('h1.for-desktop::text').get()
        item['price'] = response.css('#sellingPWeb::text').get()
        item['rating'] = starCount.extract()

        yield item






