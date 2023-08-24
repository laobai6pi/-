# 开发时间: 2023-08-21 17:54
import scrapy
from web_crawler.items import ProductItem

class NordstromSpider(scrapy.Spider):
    name = 'nordstrom'
    allowed_domains = ['nordstrom.com']
    start_urls = ['https://www.nordstrom.com/browse/men/shoes/boots?breadcrumb=Home%2FMen%2FShoes%2FBoots&origin=topnav']

    def parse(self, response):
        # 在此处解析列表页，提取详情页的URL
        detail_urls = response.css('a.product-link::attr(href)').getall()
        yield from response.follow_all(detail_urls, self.parse_detail)

    def parse_detail(self, response):
        # 在此处解析详情页，提取所需信息并返回Item
        item = ProductItem()
        item['title'] = response.css('h1.product-title::text').get()
        item['price'] = response.css('span.price::text').get()
        item['color'] = response.css('span.color::text').get()
        item['size'] = response.css('span.size::text').get()
        item['sku'] = response.css('span.sku::text').get()
        item['details'] = response.css('div.details::text').get()
        item['img_urls'] = response.css('img.product-image::attr(src)').getall()
        yield item