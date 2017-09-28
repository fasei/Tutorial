# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import  Selector
import json
from tutorial.spiders import urlSetting,contentSetting
from tutorial.items import DgspiderUrlItem
from scrapy.http import Request
import os
'''
--------------------------
1、启动当前爬虫的命令如下：
通过读取上一个爬虫获取的url，自动爬取内容
scrapy crawl DgContentSpider -o all.json
2、内容介绍：仅仅能够使用针对的地址，需要配合使用dmoz_spider使用
--------------------------
'''
class WebTextSpider(scrapy.Spider):
    print('start DgContentSpider')
    # 爬虫名 必须静态指定
    # name = contentSettings.SPIDER_NAME
    name = 'WebTextSpider'
    allowed_domains=['wcxrc.com']

    # 爬取地址
    # start_urls = ['http://www.mama.cn/baby/art/20140829/774422.html']
    '''
    //1-  http://www.wcxrc.com/thread0806.php?fid=20
      2-  http://www.wcxrc.com/thread0806.php?fid=20&search=&page=2
    
    '''
    tem_url=[]
    tem_url.append('http://www.wcxrc.com/thread0806.php?fid=20')
    for i in range(2,22):
        tem_url.append('http://www.wcxrc.com/thread0806.php?fid=20&search=&page='+ str(i) )

    print(tem_url)


    start_urls = tem_url
    # start_urls_tmp = []
    # """构造分页序列，一般来说遵循规则 url.html,url_2.html,url_3.html，并且url.html也写为url_1.html"""
    # for i in range(6, 1, -1):
    #     start_single = tmp_url_list[:-5]
    #     start_urls_tmp.append(start_single + "_" + str(i) + ".html")

    def parse(self, response):
        item_url = DgspiderUrlItem()
        sel = Selector(response)
        #http://www.wcxrc.com/htm_data/20/1708/2594900.html
        url=sel.xpath('//tr[@class="tr3 t_one tac"]/td[@class="tal"]/h3/a/@href').extract()
        urls=[]
        for i in range(len(url)):
            urls.append("http://www.wcxrc.com/"+url[i])
        item_url['url']=urls

        yield item_url