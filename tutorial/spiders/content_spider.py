# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import  Selector
import json
from tutorial.spiders import urlSetting,contentSetting
from tutorial.items import DgspiderPostItem
from scrapy.http import Request

import os
# print os.getcwd()#获得当前工作目录
# print os.path.abspath('.')#获得当前工作目录
# print os.path.abspath('..')#获得当前工作目录的父目录
# print os.path.abspath(os.curdir)#获得当前工作目录

#当前文件的路径
pwd = os.getcwd()
print('pwd:',pwd)
#当前文件的父路径
# father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
#当前文件的前两级目录

grader_father=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
grader_father=os.path.abspath(os.path.dirname(pwd))


#/Users/zhuyuanyuan/PycharmProjects/tutorial
print('grader_father:',grader_father)
father_path=os.path.abspath(os.path.dirname(grader_father)+os.path.sep+".")

#/Users/zhuyuanyuan/PycharmProjects
print('father_path:',father_path)

import  sys
path = sys.path[0]
print('path',path)
#/Users/zhuyuanyuan/PycharmProjects/tutorial/tutorial/spiders
print('s.getcwd():',os.getcwd())
print('os.path.abspath(os.curdir):',os.path.abspath(os.curdir))
# --------------------------
#  启动当前爬虫的命令如下：
#   通过读取上一个爬虫获取的url，自动爬取内容
#  scrapy crawl DgContentSpider -o all.json
# --------------------------
class DgContentSpider(scrapy.Spider):
    print('start DgContentSpider')

    FEED_EXPORT_ENCODING = 'utf-8'
    with open(os.getcwd()+os.sep+'item0.json','r') as  f:
        mess=json.load(f)

    tmp_url_lists = []
    for msg in mess:
        line = msg['url']
        for i in range(len(line)):
            tmp_url_lists.append(line[i])

    # 爬虫名 必须静态指定
    # name = contentSettings.SPIDER_NAME
    name = 'DgContentSpider'

    # 设定爬取域名范围
    allowed_domains = [contentSetting.DOMAIN]

    # 爬取地址
    # start_urls = ['http://www.mama.cn/baby/art/20140829/774422.html']
    print(len(tmp_url_lists))
    start_urls = tmp_url_lists
    # start_urls_tmp = []
    # """构造分页序列，一般来说遵循规则 url.html,url_2.html,url_3.html，并且url.html也写为url_1.html"""
    # for i in range(6, 1, -1):
    #     start_single = tmp_url_list[:-5]
    #     start_urls_tmp.append(start_single + "_" + str(i) + ".html")

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
        #
        # yield items
        # Request("Some_link_goes_here", callback=self.parse_link, meta={'l': items})
        # sel : 页面源代码
        # sel = Selector(response)
        #
        # item['url'] = DgContentSpider.url
        #
        # # 对于title, <div><h1><span aaa><span>标题1</h1></div>,使用下列方法取得
        # data_title_tmp = sel.xpath(contentSetting.POST_TITLE_XPATH)
        # item['title'] = data_title_tmp.xpath('string(.)').extract()
        #
        # item['text'] = sel.xpath(contentSetting.POST_CONTENT_XPATH).extract()
        #
        # yield item
        #
        # if self.start_urls_tmp:
        #     url = self.start_urls_tmp.pop()
        #     yield Request(url, callback=self.parse)
