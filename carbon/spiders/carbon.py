import scrapy
from ..items import CarbonItem


class Carbon(scrapy.Spider):
    name="carbon38"
    start_urls=["https://www.carbon38.com/shop-all-activewear/tops"]


    def parse(self, response):
        items = CarbonItem()


        product_name=response.css('.Heading a::text').extract()  
        product_price=response.css('.Price').css('::text').extract()
        product_size=response.css('a.add-size-to-cart::text').extract()
        product_imagelink=response.css('.ProductItem__Image--alternate::attr(src)').extract()
        product_designer=response.css('.ProductItem__Designer::text').extract() 

        items['product_designer']=product_designer 
        items['product_name']=product_name 
        items['product_price']=product_price
        items['product_size']=product_size
        items['product_imagelink']=product_imagelink 

        yield items
