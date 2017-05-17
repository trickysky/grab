# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import random

from scrapy import signals
# from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class CommonRequestMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        # print 'this is common request'
        user_agent_list = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'user_agent.cfg')).read().split('\n')
        ua = random.choice(user_agent_list)
        if ua:
            request.headers['User-Agent'] = ua
        request.headers['Accept'] = '*/*'
        request.headers['Accept-Encoding'] = 'gzip, deflate, sdch'
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
        request.headers['Connection'] = 'keep-alive'
        return


class ProxyMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        # print 'this is proxy middleware'
        proxy_url = 'http://pi.tiankun.me:1081'
        request.meta['proxy'] = proxy_url
        return


class SpidermanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
