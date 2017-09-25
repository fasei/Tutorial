import scrapy
from tutorial.items import DmozItem,DgspiderUrlItem
from scrapy.selector import  Selector
from tutorial.spiders import urlSetting

# import os
# print os.getcwd()#获得当前工作目录
# print os.path.abspath('.')#获得当前工作目录
# print os.path.abspath('..')#获得当前工作目录的父目录
# print os.path.abspath(os.curdir)#获得当前工作目录



#启动当前模块    Scrapy crawl DgUrlSpider
class DmozSpider(scrapy.Spider):

    #爬虫名称，需要静态指定
    name=urlSetting.SPIDER_NAME

    #设定域名
    allowed_domains=[urlSetting.DOMAIN]

    '''
    一般来说，列表页 第一页不符合规范，单独append
    '''
    url_list=[]
    url_list.append(urlSetting.START_LIST_URL)
    loop=urlSetting.LIST_URL_RULER_LOOP

    #生成分页的url
    for i in range(2,loop):
        url=urlSetting.LIST_URL_RULER_PREFIX+str(i)+urlSetting.LIST_URL_RULER_SUFFIX
        url_list.append(url)

    start_urls=url_list

    # 1、直接指定url
    # start_urls=[
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]


    def parse(self, response):
        #sel:页面源代码
        print('rrrrrrrrrrr',response)
        sel=Selector(response)
        item_url=DgspiderUrlItem()

        url_item=[]

        #XPATH获取url,注意 extract（）才能转成str字符串
        url_list=sel.xpath(urlSetting.POST_URL_XPATH).extract()
        print('ssss',url_list)

        #消除http前缀差异
        for url in url_list:
            url=url.replace('http:','')
            url_item.append('http:'+url)

        #list去重
        url_item=list(set(url_item))
        item_url['url']=url_item
        yield item_url






        # filename=response.url.split("/")[-2]
        # with open(filename,"wb") as f:
        #     f.write(response.body)

        # for sel in response.xpath('//ul/li'):
        #     item = DmozItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item

