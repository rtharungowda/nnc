import glob
import os
from sklearn.model_selection import KFold

#find all images in directory
imgs_list = glob.glob("/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/imgs/*.jpg")
print(f"Total number of images {len(imgs_list)}")

#kfold obj
kf =KFold(n_splits=5, shuffle=True, random_state=42)

for k,(train_ind, test_ind) in enumerate(kf.split(imgs_list)):
    print(f"fold {k} number of training images {len(train_ind)} and number of validation images {len(test_ind)}")

    #trainging .txt file
    pth = f"/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/train_yolo_{str(k)}.txt"
    if os.path.exists(pth):
        os.remove(pth)
    for i in train_ind:
        with open(pth, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            file_object.write(imgs_list[i])
    
    #validation .txt file
    pth = f"/content/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/related_files/val_yolo_{str(k)}.txt"
    if os.path.exists(pth):
        os.remove(pth)
    for i in test_ind:
        with open(pth, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            file_object.write(imgs_list[i])
    