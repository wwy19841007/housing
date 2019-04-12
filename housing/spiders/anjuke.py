# -*- coding: utf-8 -*-
import scrapy
from housing.items import House
import sys
import os
import io

reload(sys)
sys.setdefaultencoding( "utf-8" )

class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://xm.anjuke.com/sale/p1-rd1/?kw=%E8%8E%B2%E8%8A%B1#filtersort'
                  ]
    result = "type,address,model,size,price,unitprice,url\r\n"

    def parse(self, response):
        for item in response.xpath('//li[@class="list-item"]'):
            house = House()
            type = item.xpath('.//div[@class="house-title"]/a/@title').extract()[0].replace('\n', '').replace(' ', '').replace(',', '')
            print(type)
            house["type"] = type
            address = item.xpath('.//span[@class="comm-address"][@title]/text()').extract()[0].replace('\n', '').replace(' ', '').replace(',', '')
            print(address)
            house["address"] = address
            model = item.xpath('.//div[@class="details-item"]/span/text()').extract()[0].replace('\n', '').replace(' ', '').replace(',', '')
            print(model)
            house["model"] = model
            size = item.xpath('.//div[@class="details-item"]/span/text()').extract()[1].replace('\n', '').replace(' ', '').replace(',', '')
            print(size)
            house["size"] = size
            price = item.xpath('.//span[@class="price-det"]/strong/text()').extract()[0].replace('\n', '').replace(' ', '') + item.xpath('.//span[@class="price-det"]/text()').extract()[0].replace('\n', '').replace(' ', '')
            print(price)
            house["price"] = price
            unitprice = item.xpath('.//span[@class="unit-price"]/text()').extract()[0].replace('\n', '').replace(' ', '')
            print(unitprice)
            house["unitprice"] = unitprice
            url = item.xpath('.//div[@class="house-title"]/a/@href').extract()[0].replace('\n', '').replace(' ', '')
            print(url)
            house["url"] = url
            self.result += type + "," + address + "," + model + "," + size + "," + price + "," + unitprice + "," + url + "\r\n"
            # yield house


        # filename = response.url.split("/")[-2] + ".htm"
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        curr = response.xpath('//i[@class="curr"]/text()').extract_first()
        if curr is not None and int(curr) < 50:
            next_page_url = 'https://xm.anjuke.com/sale/p' + str((int(curr) + 1)) + '-rd1/?kw=%E8%8E%B2%E8%8A%B1#filtersort'
            yield scrapy.Request(response.urljoin(next_page_url))
        else:
            filename = os.path.realpath("") + "\\tmp\\result.txt"
            with io.open(filename, 'wb') as f:
                f.write(self.result)
