# -*- coding: utf-8 -*-
from __future__ import absolute_import
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from kickstarter.items import KickstarterItem
import re

class Kickstarter(Spider):
    name = 'kick'
    page = 1
    max = 1
    url = 'https://www.kickstarter.com/discover/advanced?state=successful&woe_id=23424977&sort=popularity&no_stream=1&seed=2469352&page='
    start_urls = [url + str(page)]
    host = 'https://www.kickstarter.com'

    def parse(self, response):
        selector = Selector(response)
        rows = selector.xpath('//div[@class="row"]')
        for row in rows:
            projects = row.xpath('li')
            for project in projects:
                url = self.host + project.xpath('div/div[2]/div/a/@href').extract_first()
                # print '==============================='
                # print url
                # print '==============================='
                yield Request(url, callback=self.parse_page)
        if self.page < self.max:
            self.page += 1
            url = self.url + str(self.page)
            yield Request(url, callback=self.parse)

    def parse_page(self, response):
        print '============================================='
        print 'working on page %s' % str(self.page)
        print '============================================='
        item = KickstarterItem()
        selector = Selector(response)
        name = selector.xpath('//*[@id="content-wrap"]/section/div[2]/div[1]/h2/span/a/text()').extract_first()
        backer_number = selector.xpath(
            '//div[@class="col-right col-4 py3 border-left"]/div[2]/h3/text()').extract_first()

        total_mount = selector.xpath(
            '//div[@class="col-right col-4 py3 border-left"]/div[1]/h3/span/text()').extract_first()
        goal = selector.xpath(
            '//div[@class="col-right col-4 py3 border-left"]/div[1]/div[1]/span/text()').extract_first()
        time_start = selector.xpath(
            '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[3]/p/time[1]/text()').extract_first()
        time_end = selector.xpath(
            '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[3]/p/time[2]/text()').extract_first()
        period_re = re.compile(ur'\d+')
        period_data = selector.xpath(
            '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[3]/p/text()[3]').extract_first()
        period = period_re.search(period_data).group()
        created_by = selector.xpath(
            '//a[@class="hero__link remote_modal_dialog js-update-text-color"]/text()').extract_first()
        comments = selector.xpath(
            '//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[4]/@data-comments-count').extract_first()
        location = selector.xpath(
            '//a[@class="project-header-category-location-link grey-dark mr3 nowrap type-12"]/text()').extract_first()
        tag = selector.xpath(
            '//a[@class="project-header-category-location-link grey-dark mr3 nowrap type-12"][2]/text()').extract_first()

        item['name'] = name
        item['backer_number'] = backer_number
        item['total_mount'] = total_mount
        item['goal'] = goal
        item['time_start'] = time_start
        item['time_end'] = time_end
        item['period'] = period
        item['created_by'] = created_by
        item['comments'] = comments
        item['location'] = location
        item['tag'] = tag

        yield item


