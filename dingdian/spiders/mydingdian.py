import scrapy
from scrapy.http import Request
from ..items import DingdianItem


class MydingdianSpider(scrapy.Spider):
    name = 'mydingdian'
    allowed_domains = ['www.x23us.com/']
    start_url = ['https://www.x23us.com/class/']
    starturl=['.html']


    def start_requests(self):
        # for i in range(1,11):
        for i in range(5, 6):
            #print(i)
            url_con=str(i)+'_1'
            #print(url_con)
            url1 = self.start_url+list(url_con)+self.starturl
            #print(url1)
            url=''
            for j in url1:
                url+=j+''
            #print(url)
            yield Request(url, self.parse)

    def parse(self, response):

        baseurl=response.url #真正的url链接
        #print(baseurl)
        max_num = response.xpath('//*[@id="pagelink"]/a[14]/text()').extract_first()  # 获取当前页面的最大页码数
        #print(max_num) #页码数
        baseurl = baseurl[:-7]
        #print(baseurl)

        for num in range(1,int(max_num)+1):
        #for num in range(1, 5):
            #print(list("_" + str(num)))
            newurl1 = list(baseurl) + list("_" + str(num)) + self.starturl
            #print(newurl1)
            newurl=''
            for j in newurl1:
                newurl+=j+''
            print(newurl)
            # 此处使用dont_filter和不使用的效果不一样，使用dont_filter就能够抓取到第一个页面的内容，不用就抓不到
            # scrapy会对request的URL去重(RFPDupeFilter)，加上dont_filter则告诉它这个URL不参与去重。
            yield Request(newurl, dont_filter=True, callback=self.get_name)  # 将新的页面url的内容传递给get_name函数去处理

    def get_name(self,response):
        item=DingdianItem()
        for nameinfo in response.xpath('//tr'):
            #print(nameinfo)
            novelurl = nameinfo.xpath('td[1]/a/@href').extract_first()  # 小说地址
            #print(novelurl)
            name = nameinfo.xpath('td[1]/a[2]/text()').extract_first()  # 小说名字
            #print(name)
            newchapter=nameinfo.xpath('td[2]/a/text()').extract_first()   #最新章节
            #print(newchapter)
            date=nameinfo.xpath('td[5]/text()').extract_first()    #更新日期
            #print(date)
            author = nameinfo.xpath('td[3]/text()').extract_first()  # 小说作者
            #print(author)
            serialstatus = nameinfo.xpath('td[6]/text()').extract_first()  # 小说状态
            #print(serialstatus)
            serialsize = nameinfo.xpath('td[4]/text()').extract_first()  # 小说大小
            #print(serialnumber)
            #print('--==--'*10)
            if novelurl:
                item['novel_name'] = name
                #print(item['novel_name'])
                item['author'] = author
                item['novelurl'] = novelurl
                #print(item['novelurl'])
                item['serialstatus'] = serialstatus
                item['serialsize'] = serialsize
                item['date']=date
                item['newchapter']=newchapter

                print('小说名字:', item['novel_name'])
                print('小说作者:', item['author'])
                print('小说地址:', item['novelurl'])
                print('小说状态:', item['serialstatus'])
                print('小说大小:', item['serialsize'])
                print('更新日期:', item['date'])
                print('最新章节:', item['newchapter'])

                print('===='*5)

                #yield Request(novelurl,dont_filter=True,callback=self.get_novelcontent,meta={'item':item})
                yield item
                '''
    def get_novelcontent(self,response):
        #print(123124)  #测试调用成功url
        item=response.meta['item']
        novelurl=response.url
        #print(novelurl)
        serialnumber = response.xpath('//tr[2]/td[2]/text()').extract_first()  # 连载字数
        #print(serialnumber)
        category = response.xpath('//tr[1]/td[1]/a/text()').extract_first()  # 小说类别
        #print(category)
        collect_num_total = response.xpath('//tr[2]/td[1]/text()').extract_first()  # 总收藏
        #print(collect_num_total)
        click_num_total = response.xpath('//tr[3]/td[1]/text()').extract_first()  # 总点击
        novel_breif = response.xpath('//dd[2]/p[2]').extract_first()        #小说简介

        # item['serialnumber'] = serialnumber
        # item['category'] = category
        # item['collect_num_total']=collect_num_total
        # item['click_num_total']=click_num_total
        # item['novel_breif']=novel_breif
        #
        # print('小说字数:', item['serialnumber'])
        # print('小说类别:', item['category'])
        # print('总收藏:', item['collect_num_total'])
        # print('总点击:', item['click_num_total'])
        # print('小说简介:', item['novel_breif'])
        # print('===='*10)

        yield item
