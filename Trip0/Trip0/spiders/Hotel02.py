import scrapy
import re
from ..items import Trip0Item


class Hotel02Spider(scrapy.Spider):
    name = 'Hotel02'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotel_Review-g303946-d1229249-Reviews-Mercure_Vung_Tau-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d8778363-Reviews-Pullman_Vung_Tau-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d11740637-Reviews-The_Wind_Boutique_Resort-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d12850481-Reviews-The_Wind_Mountain_Side_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d19453141-Reviews-RedDoorz_Plus_near_Bai_Truoc-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d1904294-Reviews-Vung_Tau_Intourco_Resort-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d19609103-Reviews-Fusion_Suites_Vung_Tau-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d19656135-Reviews-Mermaid_Seaside_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d1488402-Reviews-The_Imperial_Hotel_Resort_Vung_Tau-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d8491228-Reviews-Thanh_Xuan_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d3912064-Reviews-Muong_Thanh_Vung_Tau_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d5617568-Reviews-Vietsovpetro_Resort-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d22939248-Reviews-Premier_Pearl_Hotel_Vung_Tau-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d10145823-Reviews-Malibu_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d21211818-Reviews-The_Cap_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d19886707-Reviews-Bao_Khoi_1_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d1885456-Reviews-Palace_Resort_Long_Hai_Beach-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d12958304-Reviews-Vung_Tau_Seaview_Homestay-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d17657451-Reviews-Hai_Phuong_Homestay-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d1934143-Reviews-Petro_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d2285747-Reviews-Green_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d23430670-Reviews-Holiday_Inn_Resort_Ho_Tram_Beach-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d13430004-Reviews-Sea_Mountain_Hotel-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d16916928-Reviews-Marina_Bay_Vung_Tau_Resort_Spa-Vung_Tau_Ba_Ria_Vung_Tau_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g303946-d10127996-Reviews-Lotus_Vung_Tau_Resort-Vung_Tau_Ba_Ria_Vung_Tau_Province.html']


    def parse(self, response):
        hotel_name = response.xpath('//h1[@id="HEADING"]/text()').get()
        #<h1 class="fkWsC b d Pn" id="HEADING">Khách sạn Imperial Vũng Tàu</h1>
        rank = response.xpath('//b[@class="rank"]/text()').get()
        #<span><b class="rank">#2</b> of 348 <a href="/Hotels-g303946-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html">Hotels in Vung Tau</a></span>
        review = response.xpath('// div[@class="cNJsa"]/text()').get()
        #<div class="cNJsa">Excellent</div>
        price = response.xpath('//b[@data-sizegroup="hr_chevron_prices"]/text()').get()
        #<div class="ui_column is-4 eBmaF Fl u"><div class="cBLdK w MKcRG"><div class="fzleB b" data-sizegroup="hr_chevron_prices">₫1,887,000</div></div></div>
        address = response.xpath('//span[@class="ceIOZ yYjkv"]/text()').get()
        #<span class="ceIOZ yYjkv">159 Thuy Van Street, Vung Tau 790000 Vietnam</span>
        review_number = response.xpath('//span[@class="btQSs q Wi z Wc"]/text()').get()
        #<a class="eJnhj P" href="#REVIEWS"><div class="cNJsa">Excellent</div><span class="ui_bubble_rating bubble_45"></span><span class="btQSs q Wi z Wc">107 reviews</span></a>
        item = Trip0Item()
        item["hotel_name"] = hotel_name
        item["rank"] = rank
        item["review"] = review
        item["price"] = price
        item["address"] = address
        item["review_number"] = review_number
        yield item
        pass