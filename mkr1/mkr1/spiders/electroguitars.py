import scrapy
from bs4 import BeautifulSoup
from mkr1.items import GuitarsItem, ShopsItem


class ElectroguitarsSpider(scrapy.Spider):
    name = "electroguitars"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/musical_instruments/elektrogitary/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        guitars_list = soup.find(class_="list-body__content content flex-wrap")

        for item in guitars_list.find_all(class_="list-item list-item--row"):
            info = item.find(class_="list-item__info")
            a = info.find("a")
            guitar_name = a.find(string=True, recursive=False).strip()
            guitar_url = a.get('href')
            guitar_url = "https://" + self.allowed_domains[0] + guitar_url
            descriptions = info.find("div", class_="specs__text")
            guitar_descriptions = descriptions.get_text().strip()

            price = item.find("div", class_="list-item__value-price text-md text-orange text-lh--1")
            guitar_price = price.get_text().strip()

            photo = item.find(class_="list-item__photo")
            image_url = photo.find(name="img").get("src")

            yield GuitarsItem(
                name=guitar_name,
                url=guitar_url,
                price=guitar_price,
                description=guitar_descriptions,
                image_urls=["https://" + self.allowed_domains[0] + image_url]
            )

            yield scrapy.Request(
                url=guitar_url,

                callback=self.parse_shops,

                meta={
                    "guitar": guitar_name
                }
            )

    def parse_shops(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        shops_list = soup.find(class_="content")

        for item in shops_list.find_all(class_="list__item row flex"):
            shop = item.find(class_="shop__header")
            a = shop.find("a")
            shop_name = a.find(string=True, recursive=False)
            shop_url = a.get('href')
            price = item.find(class_="info__price-values")
            shop_price = price.get_text().strip()

            yield ShopsItem(
                guitar=response.meta.get("guitar"),
                name=shop_name,
                url=shop_url,
                price=shop_price
            )
