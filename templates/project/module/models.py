#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30

from peewee import *
from base import DEFAULT_DB as db


class spide_table_name(Model):
    # name = CharField()

    class Meta:
        database = db


if '__main__' == __name__:
    pass
