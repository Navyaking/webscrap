import scrapy


class Carbon(scrapy.Spider):
    name="carbon38"
    start_urls=["https://www.carbon38.com/shop-all-activewear/tops"]


    def parse(self, response):
        