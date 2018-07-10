# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest

from google_scraper.items import GoogleScraperItem


class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    rotate_user_agent = True
    allowed_domains = ['google.com']

    def start_requests(self):
        words = ['Michael', 'Scrapy']
        for x in range(len(words)):
            yield SplashRequest(f'https://google.com/search?q={words[x]}&num=100')
