#!/bin/sh
nm-applet &
xset r rate 600 100 &
blueman-applet &
picom -b -c -o 0.9 -r 7 -l -1 -t -1 -f -D 10
