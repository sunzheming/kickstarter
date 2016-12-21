# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KickstarterItem(scrapy.Item):
    name = scrapy.Field()
    backer_number = scrapy.Field()
    total_mount = scrapy.Field()
    goal = scrapy.Field()
    time_start = scrapy.Field()
    time_end = scrapy.Field()
    period = scrapy.Field()
    created_by = scrapy.Field()
    comments = scrapy.Field()
    location = scrapy.Field()
    tag = scrapy.Field()

