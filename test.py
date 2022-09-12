# -*- coding: utf-8 -*-
"""
@author: Liu Sicong
"""

'''
图像去除噪声
'''
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
from skimage import measure
from PIL import Image
import cv2
import math

def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def mse(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    return mse

def nlm(X,N,K,sigma):
    H, W = X.shape
    pad_len = N+K
    Xpad=np.pad(X,pad_len,'constant',constant_values=0)
 
    yy = np.zeros(X.shape)
    B = np.zeros([H, W])
 
    for ny in range(-N, N + 1):
        for nx in range(-N, N + 1):
            # compute neighborhood SSD by looping through kernel
            # array to hold values to calculate SSD
            ssd = np.zeros((H,W))
            for ky in range(-K, K + 1):
                for kx in range(-K, K + 1):
                    ssd += np.square(
                        Xpad[pad_len+ny+ky:H+pad_len+ny+ky,pad_len+nx+kx:W+pad_len+nx+kx]
                        - Xpad[pad_len+ky:H+pad_len+ky,pad_len+kx:W+pad_len+kx])
            # compute SSD for these set of neighborhood pixels
            ex = np.exp(-ssd/(2*sigma**2))
            B += ex
            yy += ex * Xpad[pad_len+ny:H+pad_len+ny,pad_len+nx:W+pad_len+nx]
 
    return yy/B

def double2uint8(I, ratio=1.0):
    return np.clip(np.round(I*ratio), 0, 255).astype(np.uint8)

def make_kernel(f):
    kernel = np.zeros((2*f+1, 2*f+1))
    for d in range(1, f+1):
        kernel[f-d:f+d+1, f-d:f+d+1] += (1.0/((2*d+1)**2))
    return kernel/kernel.sum()

def NLmeansfilter(I, h_=10, templateWindowSize=5,  searchWindowSize=11):
    f = 2#templateWindowSize/2
    t = 5#searchWindowSize/2
    height, width = I.shape[:2]
    padLength = t+f
    I2 = np.pad(I, padLength, 'symmetric')
    kernel = make_kernel(f)
    h = (h_**2)
    I_ = I2[padLength-f:padLength+f+height, padLength-f:padLength+f+width]

    average = np.zeros(I.shape)
    sweight = np.zeros(I.shape)
    wmax =  np.zeros(I.shape)
    for i in range(-t, t+1):
        for j in range(-t, t+1):
            if i==0 and j==0:
                continue
            I2_ = I2[padLength+i-f:padLength+i+f+height, padLength+j-f:padLength+j+f+width]
            w = np.exp(-cv2.filter2D((I2_ - I_)**2, -1, kernel)/h)[f:f+height, f:f+width]
            sweight += w
            wmax = np.maximum(wmax, w)
            average += (w*I2_[f:f+height, f:f+width])
    return (average+wmax*I)/(sweight+wmax)


# img_ref = plt.imread('E:/VScode/python/cim1.bmp')
img_ref = Image.open('E:/VScode/python/cim1.bmp')
img_ref = img_ref.convert('L')
img_ref = np.asarray(img_ref, dtype=np.uint8)
# img = plt.imread('E:/VScode/python/cim1_1_5.bmp')
img = Image.open('E:/VScode/python/cim1_1_5.bmp')
img = img.convert('L')
img = np.asarray(img, dtype=np.uint8)

fig = plt.figure(figsize=(8.0,6.0))  # figsize:指定figure的宽和高，单位为英寸
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(img)
plt.title('distortion_picture')


# plt.savefig('E:/VScode/python/train_result.jpg')
# plt.imshow(img)
# plt.show()
# img.save('E:/VScode/python/train_result.jpg')
# plt.imshow(data)


###  中值滤波
median_filter_img = cv2.medianBlur(img, 3)
ax2 = fig.add_subplot(2,3,2)
ax2.imshow(median_filter_img)
plt.title('median_filter')

#### 高斯滤波
Gaussian_filter_img = cv2.GaussianBlur(img, (3,3), 0)
ax3 = fig.add_subplot(2,3,3)
ax3.imshow(Gaussian_filter_img)
plt.title('Gaussian_filter')

####　均值滤波
mean_vaule_filter = cv2.blur(img, (5,5))
ax4 = fig.add_subplot(2,3,4)
ax4.imshow(mean_vaule_filter)
plt.title('mean_vaule_filter')

#### 双边滤波
#9 邻域直径，两个 75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img,9,75,75)
ax5 = fig.add_subplot(2,3,5)
ax5.imshow(blur)
plt.title('bilatral-filter')

# ax6 = fig.add_subplot(2,3,6)
# ax6.imshow(img_ref)
# plt.title('reference_image')


# print(psnr(img_ref, img))
# print(psnr(img_ref, median_filter_img))
# print(psnr(img_ref, Gaussian_filter_img))
# print(psnr(img_ref, mean_vaule_filter))
# print(psnr(img_ref, blur))
# 28.999386658771652
# 29.301589411225322
# 28.79977569518153
# 28.619227200105506
# 28.619831250546234
print(measure.compare_psnr(img_ref, img))
print(measure.compare_psnr(img_ref, median_filter_img))
print(measure.compare_psnr(img_ref, Gaussian_filter_img))
print(measure.compare_psnr(img_ref, mean_vaule_filter))
print(measure.compare_psnr(img_ref, blur))
# 22.248821582738945
# 21.080775639025703
# 21.976026627411876
# 18.390880298934015
# 23.369955292612396

# lena_mse = measure.compare_mse(lena, lena)
print(measure.compare_mse(img_ref, img))
print(measure.compare_mse(img_ref, median_filter_img))
print(measure.compare_mse(img_ref, Gaussian_filter_img))
print(measure.compare_mse(img_ref, mean_vaule_filter))
print(measure.compare_mse(img_ref, blur))

### test the effect of nlm
# nlm_lena = nlm(img,10,4,0.6) # 22.248821582738945

# # nlm_lena = cv2.fastNlMeansDenoising(img, None, 20.0, 5, 11) # 25.74565207529522
# nlm_lena = double2uint8(NLmeansfilter(img.astype(np.float), 20.0, 5, 11)) # 25.733058881054895

lena_psnr = measure.compare_psnr(img_ref, nlm_lena)
print(lena_psnr)
ax6 = fig.add_subplot(2,3,6)
ax6.imshow(nlm_lena)
plt.title('nlm_image')

plt.show()