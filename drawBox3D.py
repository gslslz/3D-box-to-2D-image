"""
Created on 2018/12/24 15:01

@author: Conan
"""
import os
import numpy as np
import os
import sys
import cv2
from matplotlib import pyplot as plt


#def drawBox3D(corners,object_type,object_true,img):
def drawBox3D(corners,object_type,img):
    corners = corners.astype(np.int)

    pointx=corners[0].tolist()[0]
    pointy=corners[1].tolist()[0]
    if abs(pointx[3]-pointx[0])>621:
    	return
    if abs(pointx[5]-pointx[6])>621:
    	return
    cv2.line(img,(pointx[0],pointy[0]),(pointx[1],pointy[1]),(0,255,0),1)
    cv2.line(img,(pointx[1],pointy[1]),(pointx[2],pointy[2]),(0,255,0),1)
    cv2.line(img,(pointx[2],pointy[2]),(pointx[3],pointy[3]),(0,255,0),1)
    cv2.line(img,(pointx[3],pointy[3]),(pointx[0],pointy[0]),(0,255,0),1)

    cv2.line(img,(pointx[4],pointy[4]),(pointx[5],pointy[5]),(0,255,0),1)
    cv2.line(img,(pointx[5],pointy[5]),(pointx[6],pointy[6]),(0,255,0),1)
    cv2.line(img,(pointx[7],pointy[7]),(pointx[6],pointy[6]),(0,255,0),1)
    cv2.line(img,(pointx[7],pointy[7]),(pointx[4],pointy[4]),(0,255,0),1)

    cv2.line(img,(pointx[3],pointy[3]),(pointx[7],pointy[7]),(0,255,0),1)
    cv2.line(img,(pointx[2],pointy[2]),(pointx[6],pointy[6]),(0,255,0),1)
    cv2.line(img,(pointx[1],pointy[1]),(pointx[5],pointy[5]),(0,255,0),1)
    cv2.line(img,(pointx[0],pointy[0]),(pointx[4],pointy[4]),(0,255,0),1)

    font=cv2.FONT_HERSHEY_SIMPLEX 
    img=cv2.putText(img,object_type,(pointx[4],pointy[4]),font,0.5,(0,255,0),1)
    #img=cv2.putText(img,object_true,(pointx[4],pointy[4]),font,0.5,(0,255,0),1)
    return img
