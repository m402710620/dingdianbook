# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DingdianPipeline(object):
    def process_item(self, item, spider):
        print('小说名字:',item['novel_name'] )
        print('小说作者:',item['author'])
        print('小说地址:',item['novelurl'])
        print('小说状态:',item['serialstatus'])
        print('小说大小:',item['serialsize'])
        print('更新日期:', item['date'])
        print('最新章节:', item['newchapter'])

        print('小说字数:',item['serialnumber'])
        print('小说类别:',item['category'])
        print('总收藏:', item['collect_num_total'])
        print('总点击:', item['click_num_total'])
        print('小说简介:', item['novel_breif'])

        print('===='*10)
        return item
