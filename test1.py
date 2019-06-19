#-*- coding:UTF-8 -*-
import attack as yf2
from config import Settings
import  cacl as ca
import cv2
import cacl as test
def xuan(t_end):
    rows, cols = t_end.shape
    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    img1 = cv2.warpAffine(t_end, matrix, (cols, rows))
    return img1

img = test.get_screen()
template = cv2.imread('F:\yys\\baiguiend.png', 0)
h, w = template.shape[:2]  # rows->h, cols->w
# 相关系数匹配方法：cv2.TM_CCOEFF
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
print(res.max())
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

left_top = max_loc  # 左上角
print(left_top)
right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
print (right_bottom)
cv2.rectangle(img, left_top, right_bottom, 255, 2)  # 画出矩形位置
cv2.imwrite('F:\yys\end1.png',img)
