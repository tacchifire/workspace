import cv2
import numpy as np

im1 = cv2.imread('YNU_monument.jpg')
im2 = cv2.imread('stegano.jpg')

print("========")

#縦, 横, 色(三原色か)
print(im1.shape)
print(im2.shape)

#一致してたらTrue
if(im1.shape == im2.shape):
    print("True")
else:
    print("False")

print("========")

#データタイプ
print(im1.dtype)
print(im2.dtype)

#一致してたらTrue
if(im1.dtype == im2.dtype):
    print("True")
else:
    print("False\n")

print("========")

#画像の画素値がそれぞれ一致しているか
print("Pixel")
print(np.array_equal(im1, im2))

print("========")