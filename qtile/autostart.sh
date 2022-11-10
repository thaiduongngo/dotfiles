#!/usr/bin/bash

nitrogen ~/.local/share/wallpapers/ --set-scaled --random --save &
xrandr --output eDP1 --mode 1366x768 --dpi 100 &
picom -b --config ~/.config/picom/picom.conf &
