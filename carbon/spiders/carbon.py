import scrapy
from ..items import CarbonItem


class Carbon(scrapy.Spider):
    name="carbon38"
    page_number=2
    start_urls=["https://carbon38.com/collections/tops?filter.p.m.custom.available_or_waitlist=1&page=1&filter.p.m.custom.available_or_waitlist=1"]


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

        next_page='https://carbon38.com/collections/tops?filter.p.m.custom.available_or_waitlist=1&page=' + str(Carbon.page_number) +'&filter.p.m.custom.available_or_waitlist=1'
        if Carbon.page_number<50:
            Carbon.page_number+=1
            yield response.follow(next_page,callback=self.parse)