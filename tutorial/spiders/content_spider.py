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

import  sys
class DgContentSpider(scrapy.Spider):
    print('start DgContentSpider')
    result='[{"url": ["http://www.eastlady.cn/emotion/pxgx/n166202.html","http://www.eastlady.cn/emotion/pxgx/n165262.html", "http://www.eastlady.cn/emotion/pxgx/n165472.html", "http://www.eastlady.cn/emotion/pxgx/n166201.html", "http://www.eastlady.cn/emotion/pxgx/n166162.html", "http://www.eastlady.cn/emotion/pxgx/n163518.html", "http://www.eastlady.cn/emotion/pxgx/n162920.html", "http://www.eastlady.cn/emotion/pxgx/n167973.html", "http://www.eastlady.cn/emotion/pxgx/n165263.html", "http://www.eastlady.cn/emotion/pxgx/n163496.html", "http://www.eastlady.cn/emotion/pxgx/n164757.html", "http://www.eastlady.cn/emotion/pxgx/n166161.html", "http://www.eastlady.cn/emotion/pxgx/n163959.html", "http://www.eastlady.cn/emotion/pxgx/n168922.html", "http://www.eastlady.cn/emotion/pxgx/n163498.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n155391.html", "http://www.eastlady.cn/emotion/pxgx/n155564.html", "http://www.eastlady.cn/emotion/pxgx/n153655.html", "http://www.eastlady.cn/emotion/pxgx/n153269.html", "http://www.eastlady.cn/emotion/pxgx/n154239.html", "http://www.eastlady.cn/emotion/pxgx/n155220.html", "http://www.eastlady.cn/emotion/pxgx/n152755.html", "http://www.eastlady.cn/emotion/pxgx/n156102.html", "http://www.eastlady.cn/emotion/pxgx/n156123.html", "http://www.eastlady.cn/emotion/pxgx/n155818.html", "http://www.eastlady.cn/emotion/pxgx/n153654.html", "http://www.eastlady.cn/emotion/pxgx/n154241.html", "http://www.eastlady.cn/emotion/pxgx/n156100.html", "http://www.eastlady.cn/emotion/pxgx/n155221.html", "http://www.eastlady.cn/emotion/pxgx/n153268.html", "http://www.eastlady.cn/emotion/pxgx/n154764.html", "http://www.eastlady.cn/emotion/pxgx/n155817.html", "http://www.eastlady.cn/emotion/pxgx/n154765.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n157475.html", "http://www.eastlady.cn/emotion/pxgx/n157309.html", "http://www.eastlady.cn/emotion/pxgx/n157799.html", "http://www.eastlady.cn/emotion/pxgx/n157476.html", "http://www.eastlady.cn/emotion/pxgx/n156831.html", "http://www.eastlady.cn/emotion/pxgx/n157389.html", "http://www.eastlady.cn/emotion/pxgx/n157193.html", "http://www.eastlady.cn/emotion/pxgx/n156497.html", "http://www.eastlady.cn/emotion/pxgx/n158653.html", "http://www.eastlady.cn/emotion/pxgx/n156830.html", "http://www.eastlady.cn/emotion/pxgx/n156498.html", "http://www.eastlady.cn/emotion/pxgx/n157818.html", "http://www.eastlady.cn/emotion/pxgx/n156124.html", "http://www.eastlady.cn/emotion/pxgx/n157817.html", "http://www.eastlady.cn/emotion/pxgx/n157022.html", "http://www.eastlady.cn/emotion/pxgx/n157388.html", "http://www.eastlady.cn/emotion/pxgx/n158654.html", "http://www.eastlady.cn/emotion/pxgx/n159317.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n186676.html", "http://www.eastlady.cn/emotion/pxgx/n183766.html", "http://www.eastlady.cn/emotion/pxgx/n187515.html", "http://www.eastlady.cn/emotion/pxgx/n185204.html", "http://www.eastlady.cn/emotion/pxgx/n187446.html", "http://www.eastlady.cn/emotion/pxgx/n187438.html", "http://www.eastlady.cn/emotion/pxgx/n184091.html", "http://www.eastlady.cn/emotion/pxgx/n186366.html", "http://www.eastlady.cn/emotion/pxgx/n187437.html", "http://www.eastlady.cn/emotion/pxgx/n183765.html", "http://www.eastlady.cn/emotion/pxgx/n186675.html", "http://www.eastlady.cn/emotion/pxgx/n183349.html", "http://www.eastlady.cn/emotion/pxgx/n187516.html", "http://www.eastlady.cn/emotion/pxgx/n187130.html", "http://www.eastlady.cn/emotion/pxgx/n187448.html", "http://www.eastlady.cn/emotion/pxgx/n186885.html", "http://www.eastlady.cn/emotion/pxgx/n186361.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n175979.html", "http://www.eastlady.cn/emotion/pxgx/n176345.html", "http://www.eastlady.cn/emotion/pxgx/n169333.html", "http://www.eastlady.cn/emotion/pxgx/n175397.html", "http://www.eastlady.cn/emotion/pxgx/n175396.html", "http://www.eastlady.cn/emotion/pxgx/n173023.html", "http://www.eastlady.cn/emotion/pxgx/n173877.html", "http://www.eastlady.cn/emotion/pxgx/n173872.html", "http://www.eastlady.cn/emotion/pxgx/n171360.html", "http://www.eastlady.cn/emotion/pxgx/n175715.html", "http://www.eastlady.cn/emotion/pxgx/n171999.html", "http://www.eastlady.cn/emotion/pxgx/n171359.html", "http://www.eastlady.cn/emotion/pxgx/n174364.html", "http://www.eastlady.cn/emotion/pxgx/n172769.html", "http://www.eastlady.cn/emotion/pxgx/n171917.html", "http://www.eastlady.cn/emotion/pxgx/n169895.html", "http://www.eastlady.cn/emotion/pxgx/n169332.html", "http://www.eastlady.cn/emotion/pxgx/n171918.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n152653.html", "http://www.eastlady.cn/emotion/pxgx/n144914.html", "http://www.eastlady.cn/emotion/pxgx/n151311.html", "http://www.eastlady.cn/emotion/pxgx/n144030.html", "http://www.eastlady.cn/emotion/pxgx/n151673.html", "http://www.eastlady.cn/emotion/pxgx/n149686.html", "http://www.eastlady.cn/emotion/pxgx/n142365.html", "http://www.eastlady.cn/emotion/pxgx/n152652.html", "http://www.eastlady.cn/emotion/pxgx/n142810.html", "http://www.eastlady.cn/emotion/pxgx/n145457.html", "http://www.eastlady.cn/emotion/pxgx/n152337.html", "http://www.eastlady.cn/emotion/pxgx/n143092.html", "http://www.eastlady.cn/emotion/pxgx/n142364.html", "http://www.eastlady.cn/emotion/pxgx/n152612.html", "http://www.eastlady.cn/emotion/pxgx/n151310.html", "http://www.eastlady.cn/emotion/pxgx/n144915.html", "http://www.eastlady.cn/emotion/pxgx/n147774.html", "http://www.eastlady.cn/emotion/pxgx/n144151.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n162919.html", "http://www.eastlady.cn/emotion/pxgx/n160850.html", "http://www.eastlady.cn/emotion/pxgx/n159806.html", "http://www.eastlady.cn/emotion/pxgx/n160440.html", "http://www.eastlady.cn/emotion/pxgx/n159979.html", "http://www.eastlady.cn/emotion/pxgx/n160439.html", "http://www.eastlady.cn/emotion/pxgx/n161262.html", "http://www.eastlady.cn/emotion/pxgx/n160827.html", "http://www.eastlady.cn/emotion/pxgx/n159978.html", "http://www.eastlady.cn/emotion/pxgx/n162008.html", "http://www.eastlady.cn/emotion/pxgx/n159383.html", "http://www.eastlady.cn/emotion/pxgx/n159382.html", "http://www.eastlady.cn/emotion/pxgx/n161240.html", "http://www.eastlady.cn/emotion/pxgx/n160842.html", "http://www.eastlady.cn/emotion/pxgx/n161261.html", "http://www.eastlady.cn/emotion/pxgx/n159805.html", "http://www.eastlady.cn/emotion/pxgx/n161241.html", "http://www.eastlady.cn/emotion/pxgx/n161059.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n181128.html", "http://www.eastlady.cn/emotion/pxgx/n181894.html", "http://www.eastlady.cn/emotion/pxgx/n182301.html", "http://www.eastlady.cn/emotion/pxgx/n182692.html", "http://www.eastlady.cn/emotion/pxgx/n181127.html", "http://www.eastlady.cn/emotion/pxgx/n178523.html", "http://www.eastlady.cn/emotion/pxgx/n178097.html", "http://www.eastlady.cn/emotion/pxgx/n182300.html", "http://www.eastlady.cn/emotion/pxgx/n179577.html", "http://www.eastlady.cn/emotion/pxgx/n178096.html", "http://www.eastlady.cn/emotion/pxgx/n180545.html", "http://www.eastlady.cn/emotion/pxgx/n179578.html", "http://www.eastlady.cn/emotion/pxgx/n178823.html", "http://www.eastlady.cn/emotion/pxgx/n179161.html", "http://www.eastlady.cn/emotion/pxgx/n176346.html", "http://www.eastlady.cn/emotion/pxgx/n179160.html", "http://www.eastlady.cn/emotion/pxgx/n179937.html", "http://www.eastlady.cn/emotion/pxgx/n181486.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n139832.html", "http://www.eastlady.cn/emotion/pxgx/n140560.html", "http://www.eastlady.cn/emotion/pxgx/n140251.html", "http://www.eastlady.cn/emotion/pxgx/n138829.html", "http://www.eastlady.cn/emotion/pxgx/n142260.html", "http://www.eastlady.cn/emotion/pxgx/n139735.html", "http://www.eastlady.cn/emotion/pxgx/n137024.html", "http://www.eastlady.cn/emotion/pxgx/n136954.html", "http://www.eastlady.cn/emotion/pxgx/n136953.html", "http://www.eastlady.cn/emotion/pxgx/n137657.html", "http://www.eastlady.cn/emotion/pxgx/n136629.html", "http://www.eastlady.cn/emotion/pxgx/n135999.html", "http://www.eastlady.cn/emotion/pxgx/n140252.html", "http://www.eastlady.cn/emotion/pxgx/n137819.html", "http://www.eastlady.cn/emotion/pxgx/n142277.html", "http://www.eastlady.cn/emotion/pxgx/n142018.html", "http://www.eastlady.cn/emotion/pxgx/n137023.html", "http://www.eastlady.cn/emotion/pxgx/n136630.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n134723.html", "http://www.eastlady.cn/emotion/pxgx/n133475.html", "http://www.eastlady.cn/emotion/pxgx/n133342.html", "http://www.eastlady.cn/emotion/pxgx/n132479.html", "http://www.eastlady.cn/emotion/pxgx/n129883.html", "http://www.eastlady.cn/emotion/pxgx/n129882.html", "http://www.eastlady.cn/emotion/pxgx/n132373.html", "http://www.eastlady.cn/emotion/pxgx/n127800.html", "http://www.eastlady.cn/emotion/pxgx/n127657.html", "http://www.eastlady.cn/emotion/pxgx/n129216.html", "http://www.eastlady.cn/emotion/pxgx/n127303.html", "http://www.eastlady.cn/emotion/pxgx/n135741.html", "http://www.eastlady.cn/emotion/pxgx/n129700.html", "http://www.eastlady.cn/emotion/pxgx/n132823.html", "http://www.eastlady.cn/emotion/pxgx/n135742.html", "http://www.eastlady.cn/emotion/pxgx/n132822.html", "http://www.eastlady.cn/emotion/pxgx/n133343.html", "http://www.eastlady.cn/emotion/pxgx/n127465.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n124359.html", "http://www.eastlady.cn/emotion/pxgx/n127171.html", "http://www.eastlady.cn/emotion/pxgx/n125072.html", "http://www.eastlady.cn/emotion/pxgx/n125022.html", "http://www.eastlady.cn/emotion/pxgx/n126803.html", "http://www.eastlady.cn/emotion/pxgx/n125023.html", "http://www.eastlady.cn/emotion/pxgx/n124412.html", "http://www.eastlady.cn/emotion/pxgx/n125097.html", "http://www.eastlady.cn/emotion/pxgx/n125021.html", "http://www.eastlady.cn/emotion/pxgx/n124410.html", "http://www.eastlady.cn/emotion/pxgx/n124720.html", "http://www.eastlady.cn/emotion/pxgx/n124411.html", "http://www.eastlady.cn/emotion/pxgx/n126186.html", "http://www.eastlady.cn/emotion/pxgx/n125921.html", "http://www.eastlady.cn/emotion/pxgx/n125073.html", "http://www.eastlady.cn/emotion/pxgx/n126185.html", "http://www.eastlady.cn/emotion/pxgx/n125922.html", "http://www.eastlady.cn/emotion/pxgx/n126181.html"]},{"url": ["http://www.eastlady.cn/emotion/pxgx/n191566.html", "http://www.eastlady.cn/emotion/pxgx/n188715.html", "http://www.eastlady.cn/emotion/pxgx/n187852.html", "http://www.eastlady.cn/emotion/pxgx/n190013.html", "http://www.eastlady.cn/emotion/pxgx/n191935.html", "http://www.eastlady.cn/emotion/pxgx/n187959.html", "http://www.eastlady.cn/emotion/pxgx/n191564.html", "http://www.eastlady.cn/emotion/pxgx/n187853.html", "http://www.eastlady.cn/emotion/pxgx/n190168.html", "http://www.eastlady.cn/emotion/pxgx/n187958.html", "http://www.eastlady.cn/emotion/pxgx/n189895.html", "http://www.eastlady.cn/emotion/pxgx/n191864.html", "http://www.eastlady.cn/emotion/pxgx//n191522.html", "http://www.eastlady.cn/emotion/pxgx/n191519.html", "http://www.eastlady.cn/emotion/pxgx/n191863.html", "http://www.eastlady.cn/emotion/pxgx/n188521.html", "http://www.eastlady.cn/emotion/pxgx/n192187.html", "http://www.eastlady.cn/emotion/pxgx/n188716.html"]}]'
    # 读取字符串转json对象
    mess = json.loads(result)

    # with open(sys.path[1]+'\item0.json','r') as  f:
    #     mess=json.load(f)

    tmp_url_lists = []
    for msg in mess:
        line = msg['url']
        for i in range(len(line)):
            print(type(line[i]))
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
    """对于爬去网页，无论是否爬取成功都将设置status为1，避免死循环"""


    # 爬取方法
    def parse(self, response):
        items = DgspiderPostItem()
        items['url'] = 'text'
        items['title'] = 'aaa'
        items['text'] = 'text'


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
