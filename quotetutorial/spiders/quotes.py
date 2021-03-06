# -*- coding: utf-8 -*-
import scrapy

from quotetutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css(".quote")
        ##获得class=quote的区块,迭代查询
        for quote in quotes:
            item = QuoteItem()
            text = quote.css(".text::text").extract_first()##css选择器，::scrapy 特有语法结构，获取class=test里的文本内容,extract_first方法拿到内容；
            author = quote.css(".author::text").extract_first()
            tags = quote.css(".tags .tag::text").extract()##tags是多级的，css级联；extract()提取全部内容；
            item["text"] = text
            item["author"] = author
            item["tags"] = tags
            yield item

        next=response.css(".pager .next a::attr(href)").extract_first()##链接提取，attr(属性名称)
        url=response.urljoin(next)##urljoin方法获取绝对链接
        yield scrapy.Request(url=url,callback=self.parse)#回调自己，完成递归的调用



