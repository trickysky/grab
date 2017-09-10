#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/9/8

import psycopg2

class PostgreSQL(object):
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.password = password
        self.user = user
        self.dbname = dbname
        self.host = host
        self.port = port

    def execute(self, sql):
        conn = psycopg2.connect(host=self.host, port=self.port, dbname=self.dbname, user=self.user, password=self.password)
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
        conn.close()
        return True

    def fetch(self, sql):
        conn = psycopg2.connect(host=self.host, port=self.port, dbname=self.dbname, user=self.user,
                                password=self.password)
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()
        conn.close()
        return result


if '__main__' == __name__:
    db = PostgreSQL('mydb', 'tk', 'tk0306')
    db.execute('CREATE SCHEMA IF NOT EXISTS tmp;')
    a = db.fetch('select version();')