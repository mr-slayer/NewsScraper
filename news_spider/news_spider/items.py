# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    head = scrapy.Field()
    news = scrapy.Field()
    # heading=scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()
    
