# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request


class Image360Pipeline(object):
    def process_item(self, item, spider):
        image_type = '.' + item['url'].split('.')[4]
        image_name = item['title'] + image_type
        dir_path = 'I:/360图片'
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        image_path = os.path.join(dir_path, image_name)
        urllib.request.urlretrieve(item['url'], image_path)
