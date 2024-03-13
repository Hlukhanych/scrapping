# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from lab2.items import FacultyItem

class NamePipeline:
    def process_item(self, item, spider):
        if item['name'] == '':
            item['name'] = "Невідома назва"
        return item

class MySqlPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="scrapy"
        )
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to MySQL ")
        # self.cursor.execute("USE scrapy;")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        faculty_items (
            id INT AUTO_INCREMENT,
            PRIMARY KEY (id),
            name VARCHAR(50) NOT NULL,
            url VARCHAR(500)
        );""")
        spider.logger.info("DB is ready ")

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from MySQL ")

    def process_item(self, item, spider):
        if isinstance(item, FacultyItem):
            self.cursor.execute(
                "INSERT INTO faculty_items (name, url) VALUES (%s, %s);",
                [item.get("name"), item.get("url")])

        self.connection.commit()
        return item

class Lab2Pipeline:
    def process_item(self, item, spider):
        return item
