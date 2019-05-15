# -*- coding: utf-8 -*-
"""
Created on 2018/12/24 15:01

@author: Conan
"""
import os
import numpy as np
import sys
import math

def projectToImage(pts_3D, P):
    pts_2D = np.dot(P , np.vstack((pts_3D, np.ones((1,pts_3D.shape[1])))))
    pts_2D[0] = pts_2D[0]/pts_2D[2]
    pts_2D[1] = pts_2D[1]/pts_2D[2]
    pts_2D = np.delete(pts_2D,2,axis=0)
    return pts_2D