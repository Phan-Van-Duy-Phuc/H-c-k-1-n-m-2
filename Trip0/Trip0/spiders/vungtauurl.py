from typing import NewType
import scrapy
from ..items_url import HotelurlItem

class VungtauurlSpider(scrapy.Spider):
    name = 'vungtauurl'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g303946-oa-0-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-30-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-60-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-90-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-120-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-150-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-180-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-210-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-240-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-270-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-300-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-330-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-360-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-390-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-420-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-450-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-480-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-510-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-540-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-570-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-600-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-630-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-660-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-690-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-720-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-750-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-780-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-810-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-840-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-870-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-900-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-930-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-960-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-990-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1020-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1050-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1080-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1110-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1140-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1170-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1200-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
'https://www.tripadvisor.com/Hotels-g303946-oa-1230-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html',
]

    def parse(self, response):
        links = response.xpath ('//div[@data-prwidget-name="meta_hsx_responsive_listing"]/div/div/div/div/a/@href').getall()
        for link in links:
            vungtauurl = link
            items = HotelurlItem()
            items['vungtauurl']= vungtauurl
            yield items
        pass
