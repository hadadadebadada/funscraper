import scrapy
from scrapy import item
from scrapy.loader import ItemLoader

from funscraper.items import SimpleItem


class Event_Data_Spider_Test(scrapy.Spider):
    name = 'bbc'
    start_urls = ['https://www.bbc.com/']


    def parse(self, response):
        mylist = response.xpath('//*[@id="page"]/section[3]/div/ul/li[1]/div')

        for link in mylist:
            item = SimpleItem()
            item['title'] = link.xpath('//*[@class="media__summary"]//text()').extract()
            item['title2'] = link.xpath('//*[@class="media__link"]//text()').extract()
           # item['link'] = link.xpath('@href').extract()
            yield item



        # for aTag in mylist:
        #
        #    item['event_text'] = aTag.xpath('text()').extract()

        #https://stackoverflow.com/questions/60240983/scrapy-selector-for-text-between-two-html-elements
        # tr3_text_box = response.xpath('//*[@id="content"]/main/div/div[2]/div[2]/table')
        # for p in tr3_text_box.xpath('p//text()'):
        #    item['event_text'] = p.get()
        #
        # sel = response.xpath('//*[@id="content"]/main/div/div[2]/div[2]/table')
        #
        # for tr in sel.css('tr//text()'):
        #    item['event_text'] = tr.get()

        #//*[@id="content"]/main/div/div[2]/div[2]/table/tbody/tr[3]/td[2]

        #yield item
