#!/bin/sh
sed -i \
         -e 's/#44515d/rgb(0%,0%,0%)/g' \
         -e 's/#ceada8/rgb(100%,100%,100%)/g' \
    -e 's/#44515d/rgb(50%,0%,0%)/g' \
     -e 's/#ff809c/rgb(0%,50%,0%)/g' \
     -e 's/#485663/rgb(50%,0%,50%)/g' \
     -e 's/#ceada8/rgb(0%,0%,50%)/g' \
	"$@"
