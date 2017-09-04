#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import redis
import pytz, datetime

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
t = pytz.timezone('Asia/Shanghai').localize(datetime.datetime.strptime('201709032240', '%Y%m%d%H%M'))
b = r.get('a')
resule = str(t) == b
print
