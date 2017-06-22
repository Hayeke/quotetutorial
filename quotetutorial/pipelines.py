# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TextPipeline(object):
    def __init__(self):
        self.limit = 50
    def process_item(self, item, spider):
        if item["text"]:
            if len(item["text"])>self.limit:
                item["text"] = item["text"].[0:self.limit].rstrip()+"..."
            return item
        else:
            return DropItem("")

class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(self,crawler):##自带方法，可以从settings里获取配置信息;类方法，返回一个class对象
        return cls(
            mongo_url=crawler.settings.get("MONGO_URL"),##在settings加入这两个变量
            mongo_db=crawler.settings.get("MONGO_DB")
        )
    #open_spider,定义spider启动时的操作,初始化声明
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        self.db["quotes"].insert(dict(item))
        return item
