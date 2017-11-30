#!/usr/bin/env bash

#file='/Users/tk/Downloads/osm'
file='/nas/tiankun/maptile/osm'

min_x=219321
max_x=219710
min_y=106972
max_y=107254
z=18

#min_x=219279
#max_x=219944
#min_y=106888
#max_y=107555
#z=18

for (( x = min_x; x <= max_x; x++ )); do
    mkdir -p ${file}/${z}/${x}
    for (( y = min_y; y <= max_y; y++ )); do
        echo z=$z, x=$x, y=$y
        `curl -o ${file}/${z}/${x}/${y}.png http://a.tile.openstreetmap.org/$z/$x/$y.png`
    done;
done;