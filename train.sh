#!/bin/sh

#cd back to home
cd /content/

#clone repo yolo v5 
git clone https://github.com/ultralytics/yolov5.git

#install requirements
cd /content/yolov5/
pip3 install -r requirements.txt

#download weights
python3 - <<EOF
from utils.google_utils import attempt_download

for x in ['s', 'm', 'l', 'x']:
    attempt_download(f'yolov5{x}.pt')

EOF

#start training
BATCH_SIZE="8"
NUM_EPOCHS="1"
TRAIN_YAML="/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/diatom.yaml"
CLF="/content/yolov5/models/yolov5m.yaml"
WEIGHTS="/content/yolov5/yolov5m.pt"
DEVICE="0"
echo "Batch size : $BATCH_SIZE"
echo "Number of epochs : $NUM_EPOCHS"
echo "Link to train yaml : $TRAIN_YAML"
echo "Classifier : $CLF"
echo "Using weights from : $WEIGHTS"
echo "Device : $DEVICE"

python3 /content/yolov5/train.py --batch $BATCH_SIZE --epochs $NUM_EPOCHS --data $TRAIN_YAML --cfg $CLF  --weights $WEIGHTS --device $DEVICE

#tensorboard
pip uninstall tensorboard
pip3 uninstall tensorboard

pip3 install tensorboard

tensorboard --logdir runs/train