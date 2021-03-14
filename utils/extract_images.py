import cv2
import time

def get_frames(path):
    cap = cv2.VideoCapture(path)
    # a variable to set how many frames you want to skip
    i = 0
    tt = 0
    frame_skip = 10
    start = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            cv2.imwrite('frame_'+str(tt)+'.jpg', frame)
            i = 0
            continue
        i += 1
        tt+=1
    print(f"time taken to process {tt} images was {time.time()-start}")
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    path = '/content/Diatom-Non-neuronal-Cognition/20x_DIC_1_5xzr.avi'
    get_frames(path)