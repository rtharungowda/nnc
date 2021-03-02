#!/bin/sh

#git setup
git config user.name rtharungowda
git config user.email rtharun.gowda.cd.ece19@itbhu.ac.in

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