#!/bin/sh

# Tried VLC cmd line but later found ffmeg is the best tool
# TODO : 1. Use select to filerting
# 1. Go over 10min->5min->1min (10kx->10x)
T_START=01:00:00
T_END=${FROM}
FNAME=$HOME/coursera/algs4partII-007/01_Week_0-__Welcome_to_Algorithms_Part_II/01_Course_Introduction_9-22.mp4

# Per min
time ffmpeg -i $FNAME -filter:v fps=fps=1/60 $PWD/ffmpeg_%0d.png

# Per sec
#time ffmpeg -i $FNAME  -filter:v fps=fps=30 $PWD/ffmpeg_%0d.png
