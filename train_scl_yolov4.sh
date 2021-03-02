#!/bin/sh

cd /content/ScaledYOLOv4/

#start training
IMG_SIZE="640"
BATCH_SIZE="8"
NUM_EPOCHS="600"
TRAIN_YAML="/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/diatom.yaml"
CLF="/content/ScaledYOLOv4/models/yolov4-csp.yaml"
WEIGHTS="''"
DEVICE="0"
echo "Batch size : $BATCH_SIZE"
echo "Number of epochs : $NUM_EPOCHS"
echo "Link to train yaml : $TRAIN_YAML"
echo "Classifier : $CLF"
echo "Using weights from : $WEIGHTS"
echo "Device : $DEVICE"

python3 /content/ScaledYOLOv4/train.py --img $IMG_SIZE --batch $BATCH_SIZE --epochs $NUM_EPOCHS --data $TRAIN_YAML --cfg $CLF --weights $WEIGHTS  --cache

#tensorboard
cd /usr/local/lib/python3.7/dist-packages/tensorboard

LOG_DIR="/content/ScaledYOLOv4/runs/train"

python3 main.py --logdir $LOG_DIR