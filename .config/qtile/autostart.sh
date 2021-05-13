#!/bin/sh
nm-applet &
xset r rate 600 100 &
picom -b -c -o 0.8 -r 7 -l -1 -t -1 -f -D 10
