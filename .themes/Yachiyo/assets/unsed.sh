#!/bin/sh
sed -i \
         -e 's/rgb(0%,0%,0%)/#44515d/g' \
         -e 's/rgb(100%,100%,100%)/#ceada8/g' \
    -e 's/rgb(50%,0%,0%)/#44515d/g' \
     -e 's/rgb(0%,50%,0%)/#ff809c/g' \
 -e 's/rgb(0%,50.196078%,0%)/#ff809c/g' \
     -e 's/rgb(50%,0%,50%)/#485663/g' \
 -e 's/rgb(50.196078%,0%,50.196078%)/#485663/g' \
     -e 's/rgb(0%,0%,50%)/#ceada8/g' \
	"$@"
