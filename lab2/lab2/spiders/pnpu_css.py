import scrapy
from lab2.items import FacultyItem, ProgramItem


class PnpuCssSpider(scrapy.Spider):
    name = "pnpu_css"
    allowed_domains = ["pnpu.edu.ua"]
    start_urls = ["https://pnpu.edu.ua/faculties"]

    def parse(self, response):
        items = response.css("div.entry themeform").css(".wp-block-columns")

        for item in items:
            fac_name = item.css('a.wp-block-columns::text').get()
            fac_url = item.css('a.wp-block-columns::attr(href)').get()
            # if fac_name == None:
            #     fac_name = response.url.split("/")[1]

            yield FacultyItem(
                name=fac_name,
                url=fac_url
            )

    #         yield scrapy.Request(
    #             url=fac_url,
    #
    #             callback=self.parse_faculty,
    #
    #             meta={
    #                 "faculty": fac_name
    #             }
    #         )
    #
    # def parse_faculty(self, response):
    #     items = response.css("wpsm_panel-body").css("a")
    #
    #     for item in items:
    #         prog_name = item.css('a::text').get()
    #         prog_url = item.css('a::attr(href)').get()
    #
    #         yield ProgramItem(
    #             name=prog_name,
    #             url=prog_url,
    #             faculty=response.meta.get("faculty")
    #         )