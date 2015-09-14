#!/bin/bash

gksudo killall kivy
sleep 1
gksudo killall -9 kivy

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
DISPLAY=:0 gksudo kivy ${DIR}/main.py
