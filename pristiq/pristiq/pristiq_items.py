# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PristiqItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    reviewer = scrapy.Field()
    condition = scrapy.Field()
    effective = scrapy.Field()
    ease = scrapy.Field()
    satisfaction = scrapy.Field()
    comment = scrapy.Field()

