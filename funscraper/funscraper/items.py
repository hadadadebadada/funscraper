# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FunscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    level = scrapy.Field()
    uid = scrapy.Field()
    pid = scrapy.Field()
    pass


class SimpleItem(scrapy.Item):
    title = scrapy.Field()
    title2 = scrapy.Field()
    level = scrapy.Field()
    uid = scrapy.Field()
    pid = scrapy.Field()
    pass

