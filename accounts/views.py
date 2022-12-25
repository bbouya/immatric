import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread

from .camera import *

from django.http import StreamingHttpResponse
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
import datetime


global capture,rec_frame, grey, switch, neg, face, rec, out

capture=0
grey=0
neg=0
face=0
switch=1
rec=0


#
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .forms import *
from .forms import UserRegistrationForm
from .decorators import unauthenticated_user
from .filters import *

mode = ''
# Create your views here.
@unauthenticated_user
def homeFn(request):
    return render(request, "accounts/homePage.html", {})

@unauthenticated_user
def registerFn(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            curr_user = form.save()
            username = form.cleaned_data.get('username')

            # customer (associated with the current registered user) created with provided minimal info during registeration
            Customer.objects.create(user = curr_user, first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'), email=form.cleaned_data.get('email') )

            messages.success(request, 'Account successfully created for ' + username)
    
    context = {'form': form}
    return render(request, 'accounts/registerPage.html', context)

@unauthenticated_user
def loginFn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid username or password!')
    
    return render(request, 'accounts/loginPage.html', {})

@login_required(login_url='login')
def logoutFn(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboardFn(request):
    return render(request, 'accounts/dashboardPage.html', {})



# video camera
#Models : 
#model_s = torch.hub.load("ultralytics/yolov5", "custom", path = "model/yolov5_plate_car.pt", force_reload=True)
#model_m = torch.hub.load("ultralytics/yolov5", "custom", path = "model/last_train.pt", force_reload=True)

#model_s = torch.hub.load("ultralytics/yolov5", "custom", path = "static/model/best.pt", force_reload=True)
#model_m = torch.hub.load("ultralytics/yolov5", "custom", path = "static/model/best.pt", force_reload=True)


#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Method for laptop camera
def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')

def select(request):
        
        if request.method == 'POST':
            if request.POST.get("select_name") == 'aaa':
                mode = 'model'
                print('plzz') 
                print(mode)
            else:
                mode = 'models'

            return render(request, 'accounts/dashboardPage.html')
        return render(request, 'accounts/dashboardPage.html')
    

def tasks(request):
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture=1

        elif  request.form.get('stop') == 'Stop/Start':
            if(switch==1):
                switch=0
                camera.release()
                cv2.destroyAllWindows()    
            else:
                camera = cv2.VideoCapture(0)
                switch=1
      
    elif request.method=='GET':
        return render(request, 'accounts/dashboardPage.html')
    return render(request, 'accounts/dashboardPage.html')
        
    