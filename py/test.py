#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import requests

URL_mobike = 'https://apiv2.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
URL = 'http://ip.cip.cc'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'user-agent': "MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
}

proxies = {
    "https": "https://27.226.181.45:808",
    # "http": "http://123.170.255.8:808",
    # "http": "http://pi.tiankun.me:1081",

}

r = requests.post(url=URL, headers=headers, proxies=proxies)
print(r.text)
