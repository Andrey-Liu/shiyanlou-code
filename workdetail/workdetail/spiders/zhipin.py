# -*- coding: utf-8 -*-
import scrapy
from workdetail.items import WorkdetailItem

class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=%E4%BF%84%E8%AF%AD&page=&ka=page']

    @property
    def start_urls(self):

        url_temp = "https://www.zhipin.com/c100010000/?query=%E4%BF%84%E8%AF%AD&page={}&ka=page-{}"

        return (url_temp.format(i+1, i+1) for i in range(10))

    def parse(self, response):
        works = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for work in works:
            item = WorkdetailItem()
            item['job_name'] = work.xpath('.//span[@class="job-name"]/text()').extract_first().strip()
            item['job_area'] = work.xpath('.//span[@class="job-area"]/text()').extract_first().strip()
            item['job_salary'] = work.xpath('.//span[@class="red"]/text()').extract_first().strip()
            item['education'] = work.xpath('.//div/div[1]/div[1]/a/div[2]/p/text()[1]').extract_first().strip()
            item['job_years'] = work.xpath('.//div/div[1]/div[1]/a/div[2]/p/text()[2]').extract_first().strip()
            item['company_name'] = work.xpath('//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[2]/div/h3/a/text()').extract_first().strip()  
            item['company_industry'] = work.xpath('.//div/div[1]/div[2]/div/p/text()[1]').extract_first().strip()
            item['company_size'] = work.xpath('.//div/div[1]/div[2]/div/p/text()[2]').extract_first().strip()
  
            yield item 
