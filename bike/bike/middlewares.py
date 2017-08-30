# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


from scrapy import signals

from base import BaseCommonRequestMiddleware, BaseProxyMiddleware


# from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class CommonRequestMiddleware(BaseCommonRequestMiddleware):
    pass


class ProxyMiddleware(BaseProxyMiddleware):
    pass

