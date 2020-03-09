# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/shiyanlou?tab=repositories']


    @property
    def start_urls(self):

        url_temp = "https://www.github.com/shiyanlou?after={}&tab=repositories"
        url_code = ['', 'Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODozMzozMiswODowMM4FkpQK', 'Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxMDo1MjowMiswODowMM4FkjQ0', 'Y3Vyc29yOnYyOpK5MjAxNC0xMi0xNVQxNDo0ODo1NyswODowMM4BrD-o', 'Y3Vyc29yOnYyOpK5MjAxNC0xMC0zMVQxNDo1OTozMCswODowMM4Bioa8']
        return (url_temp.format(url_code[i]) for i in range(5))

    def parse(self, response):
        repositories = response.xpath('//*[@id="user-repositories-list"]/ul/li')
        for repository in repositories:
            item =ShiyanlouItem()
            item['repo_name'] = repository.xpath('.//a[@itemprop="name codeRepository"]/text()').extract_first().strip()
            item['update_time'] = repository.xpath('.//@datetime').extract_first().strip()
            
            yield item
