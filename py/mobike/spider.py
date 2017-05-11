#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

import requests

proxies = {

}
URL = 'https://apiv2.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'user-agent': "MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
}

if '__main__' == __name__:
    params = {
        'longitude': '116.331551',
        'latitude': '40.002086',
        'scope': '1000'
    }
    r = requests.post(url=URL, proxies=proxies, data=params, headers=headers)
    if r.status_code == requests.codes.ok:
        response_body = r.json()
        for i in response_body.get('object'):
            print(i.get('bikeIds'), i.get('distX'), i.get('distY'))
    else:
        print('request code error: %s ' % r.status_code)

