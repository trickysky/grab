#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2017/8/30


class SiweiPipline(BasePipeline):
    def insert_item(self, item, spider):
        spider.models['speed'].create(
            city=item['city'],
            code=item['code'],
            time=item['time'],
            speed=item['speed'],
            road_name=item['road_name'],
            start_name=item['start_name'],
            end_name=item['end_name'],
            dir=item['dir'],
            b_index=item['b_index'],
            c_index=item['c_index'],
            s_index=item['s_index'],
            kind=item['kind'],
            rtic_lon_lats=item['rtic_lon_lats'],
            vkt=item['vkt']
        )

    def process_item(self, item, spider):
        self.insert_item(item, spider)
        return item