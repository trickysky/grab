#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import requests

URL_mobike = 'https://apiv2.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
# URL = 'http://ip.cip.cc'
URL = 'http://www.xicidaili.com/nn'
headers = {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    'user-agent': "MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive'
}

proxies = {
    "http": "http://pi.tiankun.me:1081",
}

r = requests.get(url=URL, headers=headers)
print(r.text)
