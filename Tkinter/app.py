import tkinter as tk
import torch
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import os

def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/home/tharun/Documents/Diatom-Non-neuronal-Cognition/Dataset/30_bbg/imgs/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 150 # Processing image for dysplaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()


def detect():
    os.system('chmod +x change_dir.sh')
    os.system(f'./change_dir.sh {image_data}')
    folders = os.listdir("/home/tharun/Documents/yolov5/runs/detect/")
    folders.sort()
    print(folders[-1])
    img_path = os.path.basename(image_data)
    text_file = img_path.split('.')[0]+'.txt'
    with open('/home/tharun/Documents/yolov5/runs/detect/'+folders[-1]+'/labels/'+text_file) as f:
        lines = f.readlines()
    
    result = tk.Label(frame,
                     text= '\nclass x    y    width  height   confidance\n').pack()

    for i in range(len(lines)):
        result = tk.Label(frame,
                     text= lines[i]).pack()

    img = Image.open("/home/tharun/Documents/yolov5/runs/detect/"+folders[-1]+"/"+img_path)
    img.show()
    

root = tk.Tk()
root.title('Portable Image Classifier')
# root.iconbitmap('class.ico')
root.resizable(False, False)
tit = tk.Label(root, text="Portable Image Classifier", padx=25, pady=6, font=("", 12)).pack()
canvas = tk.Canvas(root, height=700, width=500, bg='grey')
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10,
                        fg="white", bg="grey", command=load_img)
chose_image.pack(side=tk.LEFT)
class_image = tk.Button(root, text='Detect Diatoms',
                        padx=35, pady=10,
                        fg="white", bg="grey", command=detect)
class_image.pack(side=tk.RIGHT)
# model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=False)
root.mainloop()