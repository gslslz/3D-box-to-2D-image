# -*- coding: utf-8 -*-
"""
Created on 2018/12/24 15:01

@author: Conan
"""
import os
import numpy as np
import sys
import math

from projectToImage import projectToImage

def computeBox3D(object,P):
    '''
    face_idx = np.matrix([[1,2,6,5],
                         [2,3,7,6],
                         [3,4,8,7], 
                         [4,1,5,8]])
    '''
    R = np.matrix([[math.cos(object[13]), 0, math.sin(object[13])],
                    [0, 1,0],
                    [math.sin(object[13]), 0, math.cos(object[13])]])
    l = object[9]
    w = object[8]
    h = object[7]

    x_corners = [l/2, l/2, -l/2, -l/2, l/2, l/2, -l/2, -l/2]
    y_corners = [0,0,0,0,-h,-h,-h,-h]
    z_corners = [w/2, -w/2, -w/2, w/2, w/2, -w/2, -w/2, w/2]
    corners_3D = R*np.matrix([x_corners,y_corners,z_corners])
    
    corners_3D[0] = corners_3D[0] + object[10]
    corners_3D[1] = corners_3D[1] + object[11]
    corners_3D[2] = corners_3D[2] + object[12]
    '''
    if any(corners_3D[2]<0.1):
        corners_2D = []
        return corners_2D,face_idx
    '''
    corners_2D = projectToImage(corners_3D, P)
    #return corners_2D,face_idx
    return corners_2D

#computeBox3D(object,P)