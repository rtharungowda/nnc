import glob
import os

from sklearn.model_selection import train_test_split


def create_split(img_path,txt_path,ratio=0.2):
  #find all images in directory
  imgs_list = glob.glob(img_path+"*.jpg")
  print(f"Total number of images {len(imgs_list)}")

  #make split
  train, test = train_test_split(imgs_list,test_size=ratio, random_state=42, shuffle=True)
  print(f"Number of training images = {len(train)} and validation images = {len(test)}")

  #write to files
  pth = txt_path+"train_yolo.txt"
  if os.path.exists(pth):
      os.remove(pth)
  for i in train:
    with open(pth, "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
          file_object.write("\n")
      file_object.write(i)
    
  pth = txt_path+"val_yolo.txt"
  if os.path.exists(pth):
    os.remove(pth)
  for i in test:
    with open(pth, "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
          file_object.write("\n")
      file_object.write(i)


if __name__ == "__main__":
  img_path = "/content/Diatom-Non-neuronal-Cognition/Dataset/bbg/imgs/"
  txt_path = "/content/Diatom-Non-neuronal-Cognition/Dataset/bbg/related_files/"
  ratio = 0.2
  create_split(img_path,txt_path,ratio)