#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:48:53 2021

@author: huhan
"""
import cv2

import numpy as np
import matplotlib.pyplot as plt
import pylab
import imageio
import skimage.io
import numpy as np  
import cv2  
import os

filename = './video/v6.mp4'
save_path = './img/v6/'

# -----打开并且保存视频帧------

cap = cv2.VideoCapture(filename)  
fps = cap.get(cv2.CAP_PROP_FPS)		# 视频的帧率FPS

total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)	# 视频的总帧数
print('fps:', fps,'total_frame:',total_frame)

if cap.isOpened():  #VideoCaputre对象是否成功打开
    print('已经打开了视频文件')
    fps = cap.get(cv2.CAP_PROP_FPS)  # 返回视频的fps--帧率
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 返回视频的宽
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 返回视频的高
    print('fps:', fps,'width:',width,'height:',height)
    i=0
    while 1:
        if i==total_frame-1:
        #if i== 100:
            print('保存了视频的前i帧图像，保存结束')
            break
        else:
            i=i+1
            ret, frame = cap.read()  # 读取一帧视频
            # ret 读取了数据就返回True,没有读取数据(已到尾部)就返回False
            # frame 返回读取的视频数据--一帧数据
            a = i
            if a < 10:
                new_name = save_path + "00000" + str(a) + ".jpg"
            elif a < 100:
                new_name = save_path + "0000" + str(a) + ".jpg"
            elif a < 1000:
                new_name = save_path + "000" + str(a) + ".jpg"
            elif a < 10000:   
                new_name = save_path + "00" + str(a) + ".jpg"
                pass

            file_name=new_name
            cv2.imwrite(file_name, frame)

else:
    print('视频文件打开失败')

cap.release()  
cv2.destroyAllWindows()
'''
current_frame = cv2.imread(save_path+'000001.jpg')
previous_frame = current_frame
previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)  
#------- 进行轨迹处理
dirs = os.listdir(save_path)
dirs = sorted(dirs)
count = 0

#interval = int(total_frame/54)
interval = 100
for i in dirs:                             # 循环读取路径下的文件并筛选输出
    if os.path.splitext(i)[1] == ".jpg":   # 筛选jpg文件
        count += 1
        if count%interval ==0:
            print(i)
            current_frame = cv2.imread(save_path+i)        
            current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
            plt.imshow(current_frame_gray)
            plt.imshow(previous_frame_gray)
            frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray) #frame difference
            # here we use contour  and roi to detect the upper ball
            binaryImg = cv2.Canny(frame_diff,50,200) 
            plt.imshow(binaryImg)
            
            
            
            plt.imshow(frame_diff)
            previous_frame_gray = current_frame_gray

'''