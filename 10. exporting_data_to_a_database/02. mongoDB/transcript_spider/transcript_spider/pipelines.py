# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import logging
import pymongo


class MongoDBPipeline:
    collection_name = 'transcripts'

# == insert password where the **** is before running ==
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            "mongodb+srv://michael:****@cluster0.tytid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client['My_Database']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
