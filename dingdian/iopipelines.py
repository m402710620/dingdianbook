
from 爬虫大全.dingdian.dingdian import dbutil

#自定义的管道，将完整的爬取数据，保存到MySql数据库中
class DingdianPipeline(object):
    def process_item(self, item, spider):
        dbu = dbutil.MYSQLdbUtil()
        dbu.getConnection()  # 开启事物

        # 1.添加
        try:
            
            sql = "insert into ebook (novel_name,author,novelurl,serialstatus,serialsize,ebookdate,newchapter)values(%s,%s,%s,%s,%s,%s,%s)"
           
            dbu.execute(sql, (item['novel_name'],item['author'],item['novelurl'],item['serialstatus'],item['serialsize'],item['date'],item['newchapter']),True)
           
            dbu.commit()
            print('插入数据库成功！！')
        except:
            dbu.rollback()
            dbu.commit()  # 回滚后要提交
        finally:
            dbu.close()
        return item
