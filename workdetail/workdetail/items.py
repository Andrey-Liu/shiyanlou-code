# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkdetailItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    job_area = scrapy.Field()
    job_salary = scrapy.Field()
    education = scrapy.Field()
    job_years = scrapy.Field()
    company_name = scrapy.Field()
    company_industry = scrapy.Field()
    company_size = scrapy.Field()
    
