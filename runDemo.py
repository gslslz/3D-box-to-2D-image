# -*- coding: utf-8 -*-
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

from readCalib import readCalibration
from readLab import readLabels
from projectToImage import projectToImage
from comBox3D import computeBox3D
from computeOrientation3D import computeOrientation3D
from drawBox3D import drawBox3D

print('======= KITTI DevKit Demo =======')
root_dir = 'exmaple/'
data_set = 'training'

cam = 2
image_dir = root_dir + data_set + '/image_' + str(cam).zfill(1) + '/'
label_dir = root_dir + data_set + '/label_' + str(cam).zfill(1) + '/'
calib_dir = root_dir + data_set + '/calib' + '/'

for i in range(2001,2111):
	img_idx=i
	#P = readCalibration(calib_dir,img_idx,cam)
	P = np.matrix([[7.215377e+02, 0.000000e+00, 6.095593e+02, 4.485728e+01], [0.000000e+00, 7.215377e+02, 1.728540e+02, 2.163791e-01],[0.000000e+00, 0.000000e+00, 1.000000e+00, 2.745884e-03]])
	fid = open(label_dir + str(img_idx).zfill(6) + '.txt','r')
	img =cv2.imread(image_dir + str(img_idx).zfill(6) + '.png')
	'''
	for line in fid:
	    object_type,object_true,object = readLabels(line)
	    if float(object_true)>0.999:
	        corners = computeBox3D(object,P)
	        drawBox3D(corners,object_type,object_true,img)
	        #plt.imshow(img)
	'''
	for line in fid:
	    object_type,object = readLabels(line)
	    corners = computeBox3D(object,P)
	    drawBox3D(corners,object_type,img)
	    #plt.imshow(img)

	fid.close()
	cv2.imwrite( root_dir + data_set + '/pre_image/' +str(img_idx).zfill(6) + '.png',img)
