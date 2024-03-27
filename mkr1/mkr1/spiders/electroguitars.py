import scrapy


class ElectroguitarsSpider(scrapy.Spider):
    name = "electroguitars"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/musical_instruments/elektrogitary/"]

    def parse(self, response):
        pass
