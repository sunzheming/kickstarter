# -*- coding: utf-8 -*-

from __future__ import absolute_import
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
import re


class pagetest(Spider):
    name = 'test'
    # start_urls = ['https://www.kickstarter.com/projects/497254986/kobold-press-bestiary-a-collection-of-fantasy-mini?ref=city']
    start_urls = ['https://www.kickstarter.com/projects/ricklevine/xoab-active-fashion-meets-function?ref=city']
    def parse(self, response):
        selector = Selector(response)
        name = selector.xpath('//*[@id="content-wrap"]/section/div[2]/div[1]/h2/span/a/text()').extract_first()
        backer_number = selector.xpath('//div[@class="col-right col-4 py3 border-left"]/div[2]/h3/text()').extract_first()

        total_mount = selector.xpath('//div[@class="col-right col-4 py3 border-left"]/div[1]/h3/span/text()').extract_first()
        goal = selector.xpath('//div[@class="col-right col-4 py3 border-left"]/div[1]/div[1]/span/text()').extract_first()
        time_start = selector.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[3]/p/time[1]/text()').extract_first()
        time_end = selector.xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[3]/p/time[2]/text()').extract_first()
        period_re = re.compile(ur'\d+')
        period_data = selector.xpath(
            '//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[2]/div[3]/p/text()[3]').extract_first()
        period = period_re.search(period_data).group()
        created_by = selector.xpath('//a[@class="hero__link remote_modal_dialog js-update-text-color"]/text()').extract_first()
        comments = selector.xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[4]/@data-comments-count').extract_first()
        location = selector.xpath('//a[@class="project-header-category-location-link grey-dark mr3 nowrap type-12"]/text()').extract_first()
        tag = selector.xpath('//a[@class="project-header-category-location-link grey-dark mr3 nowrap type-12"][2]/text()').extract_first()

        print '================================='
        print '%s ||%s ||%s ||%s ||%s ||%s ||%s ||%s ||%s ||%s ||%s ' % (name, backer_number,total_mount, goal, time_start, time_end, period, created_by, comments,location, tag)
        print '================================='
# <div class="col-right col-4 py3 border-left">
# <div class="mb3">
# <h3 class="mb0">
# <span class="money">$20,338</span>
# </h3>
# <div class="type-12 medium navy-500">
# pledged of <span class="money">$7,000</span> goal
# </div>
# </div>
# <div class="mb0">
# <h3 class="mb0">
# 217
# </h3>
# <div class="type-12 medium navy-500">
# backers
# </div>
# </div>
# </div>
# //*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div/text()[2]