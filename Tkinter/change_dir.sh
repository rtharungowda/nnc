#!/bin/bash
cd ..
cd ..
ls
cd yolov5
ls

WEIGHTS="../tt_split_1000.pt"
CONF=0.4

python3 detect.py --source $1 --weights $WEIGHTS --conf $CONF --device "cpu" --save-txt --save-conf