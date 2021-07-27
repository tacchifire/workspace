import cv2
import numpy as np
from matplotlib import pyplot as plt

#元画像の読み込み(BGR順)
img = cv2.imread("元画像.jpg")

#RGB順に変換
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(rgb_img)

#R,G,Bごとに読み取り
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

#ヒストグラム化
hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])

#ヒストグラム表示
plt.plot(hist_r, color='r', label="r")
plt.plot(hist_g, color='g', label="g")
plt.plot(hist_b, color='b', label="b")
plt.legend()
plt.show()



#HSVに変換
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

