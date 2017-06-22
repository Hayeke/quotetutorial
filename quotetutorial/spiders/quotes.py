# -*- coding: utf-8 -*-
import scrapy



class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    ##负责解析
    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes: ##获得class=quote的区块,迭代查询
            text =quote.css(".text::text").extract_first()##css选择器，::scrapy 特有语法结构，获取class=test里的文本内容,extract_first方法拿到内容；
            author = quote.css(".author::text").extract_first()
            tags = quote.css(".tags .tag::text").extract()##tags是多级的，css级联；extract()提取全部内容；



