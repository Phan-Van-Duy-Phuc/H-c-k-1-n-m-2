# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Trip0Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_name = scrapy.Field()
    rank = scrapy.Field()
    review = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    review_number = scrapy.Field()
    pass