# Diatom-Non-neuronal-Cognition
https://github.com/devoworm/Proposals-Public-Lectures/blob/master/GSoC/2021/DL-for-Diatom-Non-neuronal-Cog.md

Setup:
+ Run ``` sh setup_yolov5.sh ``` for setting up and cloning yolov5 repository. OR
+ Run ``` sh setup_scl_yolov4.sh ``` for setting up and cloning Scaled yolov4 repository.

Training:
+ Make changes in **train_yolov5.sh** for training on dataset using yolov5.
  + To start training Run ``` sh train_yolov5.sh ```. OR
+ Make changes in **train_scl_yolov4.sh** for training on dataset using yolov4.
  + To start training run ``` sh train_scl_yolov4.sh ```.
 
Prediction:
+ Make changes in **predict_yolov5.sh** for predicting on dataset using yolov5. 
  + To make predicitions run ``` sh predict_yolov5.sh ```. OR
+ Make changes in **predict_scl_yolov4.sh** for predicting on dataset using yolov4.
  + To make predictions run ``` sh predict_scl_yolov4.sh ```.
