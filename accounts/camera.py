#from flask import Flask, render_template, Response, request
import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread

import io 
import os
from PIL import Image
import cv2
import numpy as np
import pandas as pd
from torchvision.models import detection
import json
import time

import torch
from torchvision import models
#from flask import  Flask, render_template, request, redirect,Response

import datetime
from .views import *

# Model de detection
model_s = torch.hub.load("ultralytics/yolov5", "custom", path = "static/model/last_train.pt", force_reload=True)
model_m = torch.hub.load("ultralytics/yolov5", "custom", path = "static/model/last_train.pt", force_reload=True)

mode = 'model'

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.mode = mode
        

    def __del__(self):
        self.video.release()

    def change_mode(self, mode):
        if mode == '':
            mode = 'model'
        else:
            mode = ''


    #This function is used in views
    def get_frame(self):
        
        success, image = self.video.read()
        frame_flip = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        img = Image.open(io.BytesIO(frame))
        if self.mode == 'model':
            results = model_s(img, size=640)
        else:
            results = model_m(img, size=640)
            text = get_plate_text(results) 
        results.print()
           
        #print('ayouuuub')
        #print(mode)
        img = np.squeeze(results.render())
        img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        frame = cv2.imencode('.jpg', img_BGR)[1].tobytes()
        
        #cv2.putText(frame,'OpenCV',(10,500), cv2.FONT_ITALIC, 4,(255,255,255),2,cv2.LINE_AA)
        return frame

# Function to get the text :
def get_plate_text(results):
    
        wow = results.pandas().xyxy[0].to_json(orient="records")  
        data = json.loads(wow) 
        text = ''
        if wow  != '[]':
                df = pd.DataFrame(data)
                df = df.sort_values('name')
                sorted_listOfDicts = df.T.to_dict().values()
                
                print('*********')
                df_sorted = df.sort_values(by=['xmin'])
                print(df_sorted.head(10)) 
                print('*********')
                text_plate = [x for x in df_sorted['name']]
                #text_plate = text_plate.join('/', text_plate)
                # using list comprehension 
                listToStr = '/'.join([str(element) for element in text_plate]) 
                inc = 0
                text = ''
                for i in text_plate:
                    if int(i) < 10:
                        text = text + i
                        
                    else : 
                        text = text + "//" + i + '//'  
        return text



