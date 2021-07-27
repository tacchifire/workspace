import cv2
import numpy as np
from matplotlib import pyplot as plt

#元画像の読み込み(BGR順)
img = cv2.imread("元画像.jpg")

#RGB順に変換
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(rgb_img)

#HSVに変換
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv_img)
