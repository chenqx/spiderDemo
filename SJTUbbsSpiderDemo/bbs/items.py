# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class BbsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url   = Field()
    forum = Field()
    poster = Field()
    content = Field()
    # postid = Field()
    # poster = Field()
    # content = Field()
    # num = Field()
    # date = Field()
    
