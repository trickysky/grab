# -*- coding: utf-8 -*-

# Scrapy settings for traffic project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

from base_settings import *

BOT_NAME = 'traffic'
# LOG_LEVEL = 'DEBUG'

SPIDER_MODULES = ['traffic.spiders']
NEWSPIDER_MODULE = 'traffic.spiders'


