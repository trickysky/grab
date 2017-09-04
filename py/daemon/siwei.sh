#!/usr/bin/env bash
date=`date -d 'yesterday' +%m%d`
export PGPASSWORD=''
psql -d mydb -U tk -c "SELECT * INTO siwei.siwei_${date} FROM traffic.spider_traffic_siwei_speed WHERE date_trunc('day', time)=date_trunc('day', now() - INTERVAL '1 day');" && psql -d mydb -U tk -c "DELETE FROM traffic.spider_traffic_siwei_speed WHERE date_trunc('day', time)=date_trunc('day', now() - INTERVAL '1 day');"&& echo complete!!