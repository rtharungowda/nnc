#!/bin/sh
i=0
while :
do 
    cp -r /content/yolov5/runs/train/exp/ /content/drive/MyDrive/Bacillaria_Paradoxa/yolo_weights/30_bbg_images/exp3
    echo "Done copying $i times"
    i=$((i+1))
    sleep 30
done    