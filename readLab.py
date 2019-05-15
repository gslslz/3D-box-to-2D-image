# -*- coding: utf-8 -*-
"""
Created on 2018/12/24 15:01

@author: Conan
"""
import os
import numpy as np
import os
import sys

def readLabels(line):
     C=line.split()
     object_type = C[0]
     #object_true = C[15]
     object = C[1:]
     for i in range(14):
         object[i]=float(object[i])
     #return object_type,object_true,object
     return object_type,object
     
'''
object_type,object = readLabels('F:/kitti/training/label_2/',0)
print(object_type,object)
'''
