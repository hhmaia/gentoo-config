#!/bin/sh

setxkbmap -option caps:swapescape &
xset r rate 300 90 &
#systemctl try-restart --user redshift &
redshift -x && redshift -o

while killall -s SIGKILL picom; do
  sleep 0.2
done
picom -b &
