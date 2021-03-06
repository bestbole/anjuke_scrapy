# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    arc = scrapy.Field()
    composition = scrapy.Field()
    price = scrapy.Field()
    floor = scrapy.Field()
    year = scrapy.Field()
    address = scrapy.Field()
    location = scrapy.Field()
    head_to = scrapy.Field()
    decoration = scrapy.Field()
    district = scrapy.Field()
    block = scrapy.Field()
    link = scrapy.Field()
    created_at = scrapy.Field()
