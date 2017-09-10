#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/9/8

# 将抓取的四维路网的字符串geom_str空间化为几何字段geom

import traffic.models as models
import utility

db = utility.PostgreSQL('mydb', 'tk', 'tk0306')

for row in models.spider_traffic_siwei_road_name.select():
    hash_code = row.hash_code
    geom_str = row.geom_str

    if geom_str:
        tmp_line_list = []
        for line_str in geom_str.split(','):
            tmp_list = []
            tmp_str = ''
            for i, point in enumerate(line_str.split()):
                if not i % 2:
                    tmp_str = point
                else:
                    tmp_str += ' %s' % point
                    tmp_list.append(tmp_str)
            tmp_line_list.append('(%s)' % ','.join(tmp_list))
        sql = """UPDATE siwei.siwei_road SET geom=public.st_setsrid(st_geomfromtext('MULTILINESTRING(%s)'), 4326) WHERE hash_code='%s';""" % (','.join(tmp_line_list), hash_code)
        db.execute(sql)
