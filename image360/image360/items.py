# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = table = 'images'
    # 图片id
    id = scrapy.Field()
    # 图片链接
    url = scrapy.Field()
    # 图片名
    title = scrapy.Field()

