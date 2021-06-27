# Diatom-Non-neuronal-Cognition
The aim of this project will be to improve upon a Deep Learning model that extracts morphological features from microscopy images of Bacillaria Paradoxa. 

## Notebooks:
<table>
<td>
<a target="_blank"  href="https://colab.research.google.com/github/rtharungowda/nnc/blob/main/diatom_object_detection.ipynb">
    <img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab - Object detection
</a>
</td>
<td>
<a target="_blank"  href="https://colab.research.google.com/github/rtharungowda/nnc/blob/main/diatom_instance_segmentation.ipynb">
    <img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab - Instance segmentation
</a>
</td>
</table>
<br>
<br>

## Run from github
### Setup:
+ Run ``` sh setup_yolov5.sh ``` for setting up and cloning yolov5 repository. OR
+ Run ``` sh setup_scl_yolov4.sh ``` for setting up and cloning Scaled yolov4 repository.

### Training:
+ Make changes in **train_yolov5.sh** for training on dataset using yolov5.
  + To start training run ``` sh train_yolov5.sh ```. OR
+ Make changes in **train_scl_yolov4.sh** for training on dataset using yolov4.
  + To start training run ``` sh train_scl_yolov4.sh ```.
 
### Prediction:
+ Make changes in **predict_yolov5.sh** for predicting on dataset using yolov5. 
  + To make predicitions run ``` sh predict_yolov5.sh ```. OR
+ Make changes in **predict_scl_yolov4.sh** for predicting on dataset using yolov4.
  + To make predictions run ``` sh predict_scl_yolov4.sh ```.
