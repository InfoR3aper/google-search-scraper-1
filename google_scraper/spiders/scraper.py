# -*- coding: utf-8 -*-
import scrapy


class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    allowed_domains = ['google.com']
    start_urls = ['https://google.com']

    def parse(self, response):
        pass
