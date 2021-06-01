import cv2
import numpy as np

#画像の指定
sample1 = "sample1.jpg" ##机の切り出し
sample2 = "sample2.jpg" ##キーボードと机の切れ目部分

#画像の読み込み(0はグレースケールでの読み込み)
spl1 = cv2.imread(sample1,0)
spl2 = cv2.imread(sample2,0)

#画像の高さ，幅
height1, width1 = spl1.shape[:3]
height2, width2 = spl2.shape[:3]

print("sample1 height:"+str(height1)+" width"+str(width1))
print("sample2 height:"+str(height2)+" width"+str(width2))

#中央値フィルタ
def median_filter(src, ksize):
    # 畳み込み演算をしない領域の幅
    # width of skip
    d = int((ksize-1)/2)
    height, width = src.shape[:3]

    # ndarray of destination
    # 出力画像用の配列（要素は入力画像と同じ）
    dst = src.copy()

    for y in range(d, height - d):
        for x in range(d, width - d):
            # 近傍にある画素値の中央値を出力画像の画素値に設定
            dst[y][x] = np.median(src[y-d:y+d+1, x-d:x+d+1])

    return dst

#中央値フィルタをかける
med1 = median_filter(spl1,5)
cv2.imwrite("med1.jpg",med1)

med2 = median_filter(spl2,10)
cv2.imwrite("med2.jpg",med2)

#エッジ検出
spl2_edge  = cv2.Canny(med2, 50, 110)

#画像の書き出し
cv2.imwrite("edge2.jpg",spl2_edge)
