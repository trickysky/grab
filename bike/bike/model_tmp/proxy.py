#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/15

from peewee import *
from base import PG_DB as db


class spider_proxy(Model):
    host = CharField(index=True)
    port = CharField(index=True)
    type = CharField(index=True)
    valid = BooleanField(index=True, default=False)
    check_time = DateTimeField(default=None, index=True, null=True)

    class Meta:
        database = db


if '__main__' == __name__:
    check_query = spider_proxy.select().where(
        (spider_proxy.host == u'49.86.62.6')
        & (spider_proxy.port == u'808')
        & (spider_proxy.type == u'https')
    )
    if check_query.exists():
        print 'exists'
    else:
        spider_proxy.create(
            host=u'49.86.62.6',
            port=u'808',
            type=u'https'
        ).execute()
