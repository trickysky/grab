#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import DEFAULT_DB as db


class spide_app_baidu(Model):
    app_id = CharField(primary_key=True)
    keyword = CharField()
    name = CharField()
    score = CharField(null=True)
    type = CharField(null=True)
    size = CharField(null=True)
    version = CharField(null=True)
    download_num = CharField(null=True)
    description = TextField(null=True)

    class Meta:
        database = db
        schema = 'app'


if '__main__' == __name__:
    pass
