# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FinalPipeline(object):
    def process_item(self, item, spider):
        return item
# class ElasticsearchPipeline(object):
#     def process_item(self, item, spider):
#         item.save_to_es()