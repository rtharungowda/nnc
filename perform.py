import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-m","--mode",
                    help="enter train for training and predict for prediction",
                    default="train",
                    type=str)
parser.add_argument("-l","--link",
                    help="link to yaml file while mode is training",
                    type=str,
                    default="/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/diatom.yaml")
parser.add_argument("-s","--source",
                    help="link to source of images for prediction",
                    type=str,
                    default="/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/imgs/")
parser.add_argument("--batch",
                    help="batch size for training",
                    type=int,
                    default=8)
parser.add_argument("--epochs",
                    help="number of epochs to train on",
                    type=int,
                    default=300)
parser.add_argument("-t","--type",
                    help="yolo model type s for small, m for medium, l for large and x for x-large",
                    type=str,
                    default="s")
parser.add_argument("-d","--device",
                    help="device to train on, 'cpu' for cpu and <gpu-index> for gpu",
                    default="cpu",
                    type=str)
parser.add_argument("-w","--weights",
                    help="link to weights.pt for prediction",
                    default="/content/yolov5/runs/train/exp/weights/best.pt",
                    type=str)
parser.add_argument("-c","--conf",
                    help="confidance score for bounding box while predicting",
                    default=0.4,
                    type=float)
args = parser.parse_args()
if args.mode == "train":
    print(f"training yolo model <{args.type}> on {args.link} yaml file, of batch size {args.batch} and for {args.epochs} epochs on device {args.device}")
    os.system(f'python3 /content/yolov5/train.py --batch {args.batch} --epochs {args.epochs} --data {args.link} --cfg /content/yolov5/models/yolov5{args.type}.yaml  --weights /content/yolov5/yolov5{args.type}.pt --device {args.device}')
else :
    print(f"predicting on images in folder {args.source} using weights {args.weights} with confidance score {args.conf}")
    os.system(f'python3 detect.py --source {args.source} --weights {args.weights} --conf {args.conf}')