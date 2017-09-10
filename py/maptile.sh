#!/usr/bin/env bash

file='/Volumes/tiankun/maptile/google_road'

min_x=219321
max_x=219710
min_y=106972
max_y=107254
z=18



for (( x = min_x; x <= max_x; x++ )); do
    mkdir -p ${file}/${z}/${x}
    for (( y = min_y; y <= max_y; y++ )); do
        echo z=$z, x=$x, y=$y
        `curl -o ${file}/${z}/${x}/${y}.png http://mt3.google.cn/vt/lyrs=m\&hl=zh-CN\&gl=cn\&x=$x\&y=$y\&z=$z\&scale=2`
    done;
done;