#!/usr/bin/bash

nitrogen ~/.local/share/wallpapers --set-scaled --random --save &
xrandr --output eDP1 --mode 1366x768 --scale 1.0 &