# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class House(scrapy.Item):
    #地址
    address = scrapy.Field()
    #房型
    type = scrapy.Field()
    #总价
    price = scrapy.Field()
    #单价
    unitPrice = scrapy.Field()
    pass
