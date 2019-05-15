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

def computeOrientation3D(object,P):
    R = np.matrix([[math.cos(object[13]), 0, math.sin(object[13])],
                    [0, 1,0],
                    [math.sin(object[13]), 0, math.cos(object[13])]])
    orientation_3D = np.matrix([[0.0, object[9]],
                                [0.0, 0.0],
                                [0.0, 0.0]])
    orientation_3D = R*orientation_3D
    
    orientation_3D[0] = orientation_3D[0] + object[10]
    orientation_3D[1] = orientation_3D[1] + object[11]
    orientation_3D[2] = orientation_3D[2] + object[12]

    '''
    if any(orientation_3D[2]<0.1):
        orientation_2D = []
        return orientation_2D
    '''
    orientation_2D = projectToImage(orientation_3D, P)
    return orientation_2D

