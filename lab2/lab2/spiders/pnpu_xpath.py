import scrapy


class PnpuXpathSpider(scrapy.Spider):
    name = "pnpu_xpath"
    allowed_domains = ["pnpu.edu.ua"]
    start_urls = ["https://pnpu.edu.ua"]

    def parse(self, response):
        pass
