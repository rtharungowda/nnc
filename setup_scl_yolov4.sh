#!/bin/sh

#git setup
git config user.name rtharungowda
git config user.email rtharun.gowda.cd.ece19@itbhu.ac.in


cd /content/

# clone Scaled_YOLOv4
git clone https://github.com/WongKinYiu/ScaledYOLOv4.git  # clone repo
cd /content/ScaledYOLOv4/
#checkout the yolov4-large branch
git checkout yolov4-large


#install mish activation funciton for cuda
cd /content/
git clone https://github.com/JunnYu/mish-cuda
cd mish-cuda
python3 setup.py build install

pip3 install -U PyYAML

#install weights
cd /content/ScaledYOLOv4/
pip3 install gdown

python3 - <<EOF
import os
if not os.path.exists("/content/ScaledYOLOv4/weights"):
    os.makedirs("/content/ScaledYOLOv4/weights/")
EOF

cd /content/ScaledYOLOv4/weights/

gdown https://drive.google.com/u/0/uc?id=1NQwz47cW0NUgy7L3_xOKaNEfLoQuq3EL