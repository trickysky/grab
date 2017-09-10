#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/5/9

str1 = 'a1 b1 a2 b2 a3 b3 a4 b4'
str2 = 'a1 b1,a2 b2,a3 b3,a4 b4'
tmp_list = []
tmp_str =''
for i, point in enumerate(str1.split()):
    if not i % 2:
        tmp_str = point
    else:
        tmp_str += ' %s' % point
        tmp_list.append(tmp_str)
print ','.join(tmp_list)

