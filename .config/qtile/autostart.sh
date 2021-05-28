#!/bin/sh
nm-applet &
blueman-applet &
xset r rate 600 100 &
~/.local/bin/picom -b
