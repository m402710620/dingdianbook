# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_name = scrapy.Field()  # 小说名字
    author = scrapy.Field()  # 作者
    novelurl = scrapy.Field()  # 小说地址
    serialstatus = scrapy.Field()  # 状态
    serialsize = scrapy.Field()  # 连载大小
    date=scrapy.Field()        #小说日期
    newchapter=scrapy.Field()   #最新章节
    serialnumber = scrapy.Field()  # 连载字数
    category = scrapy.Field()  # 小说类别
    collect_num_total = scrapy.Field()  # 总收藏
    click_num_total = scrapy.Field()  # 总点击
    novel_breif = scrapy.Field()  # 小说简介
    
