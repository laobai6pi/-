import scrapy

class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    sku = scrapy.Field()
    details = scrapy.Field()
    img_urls = scrapy.Field()