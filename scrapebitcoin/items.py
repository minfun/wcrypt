# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapebitcoinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bitcoin = scrapy.Field()
    bitprice = scrapy.Field()
    money = scrapy.Field()
