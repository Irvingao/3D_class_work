#!/usr/bin/python3
# coding=utf-8

import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 相机参数, 59.8度640x480相机
CAM_WID,CAM_HGT = 640,480           # 重投影到的深度图尺寸
CAM_FX,CAM_FY   = 795.209,793.957   # fx/fy
CAM_CX,CAM_CY   = 332.031,231.308   # cx/cy

# 加载点云数据
pc=np.genfromtxt('pc_rot.csv', delimiter=',').astype(np.float32)

# 显示加载的点云
ax = plt.figure(1).gca(projection='3d')
ax.plot(pc[:,0],pc[:,1],pc[:,2],'b.',markersize=0.1)
plt.title('point cloud')
plt.show()  

##################################################
#
# 请在这里补充代码将点云转成深度图 dep_rot
#
# 注意：下面的代码仅用于演示数据保存和显示，这些代码需要你替换
#
##################################################

# 随机生成的dep_rot, 用于演示数据保存成csv以及加载csv文件以及显示
np.random.seed(1234)
dep_rot=cv2.blur(np.random.rand(CAM_HGT,CAM_WID),(50,50))
dep_rot[dep_rot<0.5]=math.inf

# 保存重新投影生成的深度图dep_rot
np.savetxt('dep_rot.csv',dep_rot,fmt='%.12f',delimiter=',',newline='\n')

# 加载刚保存的深度图dep_rot并显示
img=np.genfromtxt('dep_rot.csv', delimiter=',').astype(np.float32)
plt.imshow(img,cmap='jet')
plt.show()


