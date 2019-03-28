# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://xm.anjuke.com/sale/p1-rd1/?kw=%E8%8E%B2%E8%8A%B1#filtersort'
                  ]

    def parse(self, response):
        for house in response.xpath('//div[@class="house-details"]/div[@class="house-title"]/a/text()'):
            print(house.extract().replace('\n', "").replace(" ", ""))
            # yield {
            #     'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
            #     'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
            #     'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            # }

        filename = response.url.split("/")[-2] + ".htm"
        with open(filename, 'wb') as f:
            f.write(response.body)
