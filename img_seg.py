import torch
import torchvision
import cv2
import argparse
from PIL import Image
import torch.nn as nn
from torchvision.transforms import transforms as transforms

if __name__=="__main__":
    # initialize the model
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True, progress=True, 
                                                            num_classes=91)
    model.roi_heads.mask_predictor.mask_fcn_logits = nn.Conv2d(256, 1, kernel_size=(1, 1), stride=(1, 1))
    print(model)
