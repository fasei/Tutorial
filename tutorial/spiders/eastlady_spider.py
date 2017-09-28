# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import  Selector
import json
from tutorial.spiders import urlSetting,contentSetting
from tutorial.items import DgspiderPostItem
from scrapy.http import Request
import os

'''
--------------------------
1、启动当前爬虫的命令如下：
通过读取上一个爬虫获取的url，自动爬取内容
scrapy crawl EastladyContentSpider -o EastladyInfo.json
2、内容介绍：仅仅能够使用针对的地址，需要配合使用dmoz_spider使用
--------------------------
'''
class EastladyContentSpider(scrapy.Spider):
    print('start EastladyContentSpider')
    name = 'EastladyContentSpider'
    # 设定爬取域名范围
    allowed_domains = ['eastlady.cn']
    # 爬取地址
    # start_urls = ['http://www.mama.cn/baby/art/20140829/774422.html']
    start_urls = []

    # 更新状态
    """对于爬取网页，无论是否爬取成功都将设置status为1，避免死循环"""


    # 爬取方法
    def parse(self, response):

        print(response.url)
        items = DgspiderPostItem()
        sel = Selector(response)

        # XPATH获取url,注意 extract（）才能转成str字符串
        items['url'] = response.url

        author = sel.xpath('//i[@class="writer ic6"]/text()')[0].extract()
        items['author'] = author

        time = sel.xpath('//i[@class="time ic6"]/text()')[0].extract()
        items['time'] = time

        title = sel.xpath(contentSetting.POST_TITLE_XPATH)[0].extract()
        items['title'] = title

        briefIntroduction = sel.xpath('//div[@class="articleI"]/text()')[0].extract()
        items['briefIntroduction'] = briefIntroduction

        tag = sel.xpath('//div[@class="articleTag w100a oh"]')[0].xpath('string(.)').extract()[0].replace('\n','').replace('标签：','').strip()
        items['tag'] = tag

        # 获取的文章都是分段的 如list样式，更新了如下新的方法，变成类似一篇文章的样式
        # text = sel.xpath(contentSetting.POST_CONTENT_XPATH).extract()
        # items['text'] = text

        #string(.)仅获取文字性描述
        text = sel.xpath(contentSetting.POST_CONTENT_XPATH)[0].xpath('string(.)')[0].extract()
        items['text'] = text



        img = sel.xpath('//div[@class="articleB"]/p/a').extract()

        imgParams=[]
        for i in range(len(img)):
            d={}
            imgLine=img[i].replace('</a>','</img></a>')
            imgSelector=Selector(text=imgLine)
            d['img_url']=imgSelector.xpath('//a/img/@src')[0].extract()
            d['img_width'] = imgSelector.xpath('//a/img/@width')[0].extract()
            d['img_height'] = imgSelector.xpath('//a/img/@height')[0].extract()
            print(d)
            imgParams.append(d)
        print(imgParams)
        items['img'] = imgParams

        print(items)
        yield items

