import face_alignment
from skimage import io
import cv2
import os
from tqdm import tqdm
if __name__ == "__main__":
    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D,device='cpu',flip_input=False)
    filename_list = os.listdir("/home/deploy/PycharmProjects/基金爬虫/Scripy/pg_data/")
    #print(filename_list)
    for filename in tqdm(filename_list):
        try:
            input = io.imread('/home/deploy/PycharmProjects/基金爬虫/Scripy/pg_data/'+filename)
            preds = fa.get_landmarks(input)
            #print(preds[0])
            img = cv2.imread('/home/deploy/PycharmProjects/基金爬虫/Scripy/pg_data/'+filename)
            #x= (max([i[0] for i in preds[0]])+min([i[0] for i in preds[0]]))/2
            #y= (max([i[1] for i in preds[0]])+min([i[1] for i in preds[0]]))/2
            x1 = max(i[0] for i in preds[0])
            x0 = min(i[0] for i in preds[0])
            y1 = max(i[1] for i in preds[0])
            y0 = min(i[1] for i in preds[0])
            print(x0,x1,y0,y1)
            print(filename.split("/")[-1])
            cropped = img[0:int(y1)+10,0:img.shape[1]]  # 裁剪坐标为[y0:y1, x0:x1]
            cv2.imwrite("../pg_data_crop/"+filename.split(".")[0]+"-crop.jpg", cropped)
        except:
            print("ERROR")
            continue

