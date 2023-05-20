#!/bin/bash
# mkardel on 20210914
# Rotate screen and stylus on x41 tablet. Tested on Debian GNU/Linux 10

xrandr_bin=/usr/bin/xrandr
xsetwacom_bin=/usr/bin/xsetwacom
stylus_id=`$xsetwacom_bin --list devices | grep STYLUS | awk '{print $7}'`
screen=LVDS1
orientation=`$xrandr_bin --verbose -q | grep LVDS | awk '{print $5}'`

# Rotate the screen and stylus, eraser and cursor, according to your preferences.
if [ "$orientation" = "normal" ]; then
	$xrandr_bin -o right
	$xsetwacom_bin set $stylus_id Rotate 1
elif [ "$orientation" = "right" ]; then
	$xrandr_bin -o inverted
	$xsetwacom_bin set $stylus_id Rotate 3
else 
	$xrandr_bin -o normal
	$xsetwacom_bin set $stylus_id Rotate 0
fi

