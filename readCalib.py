# -*- coding: utf-8 -*-
"""
Created on 2018/12/24 15:01

@author: Conan
"""
import os
import numpy as np
import sys

def readCalibration(calib_dir,img_idx,cam):
     calib = open(calib_dir + str(img_idx).zfill(6) + '.txt','r')
     aa = 0
     p = []
     for line in calib:
         bb = line.split()
         if aa == cam:
             PP = bb
             for i in range(12):
                 p.append(float(PP[i+1]))
         aa = aa + 1
     P = np.matrix([[p[0],p[1],p[2],p[3]],[p[4],p[5],p[6],p[7]],[p[8],p[9],p[10],p[11]]])
     calib.close()
     return P

'''
P=readCalibration('F:/kitti/training/calib/',0,2)
print(P)
'''