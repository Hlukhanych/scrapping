# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuitarsItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()


class ShopsItem(scrapy.Item):
    guitar = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()


class Mkr1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
