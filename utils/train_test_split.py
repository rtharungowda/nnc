import glob
from sklearn.model_selection import train_test_split

#find all images in directory
imgs_list = glob.glob("/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/imgs/*.jpg")
print(f"Total number of images {len(imgs_list)}")

#make split
train, test = train_test_split(imgs_list,test_size=0.2, random_state=42, shuffle=True)
print(f"Number of training images = {len(train)} and validation images = {len(test)}")

#write to files
for i in train:
  pth = "/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/train_yolo.txt"
  with open(pth, "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(i)
  
for i in test:
  pth = "/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/val_yolo.txt"
  with open(pth, "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(i)