import scrapy
from bs4 import BeautifulSoup
from lab2.items import FacultyItem, ProgramItem #NameItem


class PnpuSpider(scrapy.Spider):
    name = "pnpu"
    allowed_domains = ["pnpu.edu.ua"]
    start_urls = ["https://pnpu.edu.ua/faculties"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        fac_list = soup.find(class_="entry themeform")

        for item in fac_list.find_all(class_="wp-block-columns"):
            a = item.find("a")
            fac_name = a.find(string=True, recursive=False)
            fac_url = a.get('href')
            if fac_name == None:
                fac_name = response.url.split("/")[1]

            yield FacultyItem(
                name=fac_name,
                url=fac_url
            )

            yield scrapy.Request(
                url=fac_url,

                callback=self.parse_faculty,

                meta={
                    "faculty": fac_name
                }
            )

    def parse_faculty(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        prog_list = soup.find(class_="wpsm_panel-body")

        for item in prog_list.find_all("a"):
            a = item
            prog_name = a.find(string=True, recursive=False)
            prog_url = a.get('href')

            yield ProgramItem(
                name=prog_name,
                url=prog_url,
                faculty=response.meta.get("faculty")
            )

            # yield scrapy.Request(
            #     url=prog_url,
            #
            #     callback=self.parse_program,
            #
            #     meta={
            #         "program": prog_name
            #     }
            # )

    # def parse_program(self, response):
    #     soup = BeautifulSoup(response.body, 'html.parser')
    #
    #     nameP = soup.find(class_="VLoccc QDWEj U8eYrb")
    #
    #     for item in nameP.find_all("span"):
    #         span = item
    #         name = span.find(string=True, recursive=False)
    #
    #         yield NameItem(
    #             name=name,
    #             program=response.meta.get("program")
    #         )
