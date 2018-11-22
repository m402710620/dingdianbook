# dingdianbook
爬取顶点小说网的所有小说信息
在将数据存入数据库的时候会遇到 pymysql.err.InterfaceError: (0, '') 这种错误
那是因为scrapy异步的存储的原因,太快。
解决方法:只要放慢爬取速度就能解决,setting.py中设置 DOWNLOAD_DELAY = 2
