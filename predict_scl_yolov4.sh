#!/bin/sh

#cd to yolov4
cd /content/ScaledYOLOv4

#predict
IMG_SIZE="640"
SOURCE="/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/imgs"
WEIGHTS="/content/ScaledYOLOv4/runs/exp0/weights/best.pt"
CONF="0.4"

echo "Source of images : $SOURCE"
echo "Weights from : $WEIGHTS"
echo "Confindance : $CONF"

python3 /content/ScaledYOLOv4/detect.py --weights $WEIGHTS --img $IMG_SIZE --conf $CONF --source $SOURCE