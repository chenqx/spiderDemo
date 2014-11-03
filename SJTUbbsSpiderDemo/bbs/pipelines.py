# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy import log
from bbs.items import BbsItem
from twisted.enterprise import adbapi
from scrapy.contrib.exporter import XmlItemExporter
from dataProcess import dataProcess


class XmlWritePipeline(object):
    
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('bbsData.xml', 'wb')
        self.expoter = XmlItemExporter(self.file)
        self.expoter.start_exporting()

    def spider_closed(self, spider):
        self.expoter.finish_exporting()
        self.file.close()

        # process the crawled data, define and call dataProcess function
        # dataProcess('bbsData.xml', 'text.txt')

    def process_item(self, item, spider):
        self.expoter.export_item(item)
        return item
