# -*- coding:UTF-8 -*-
import os
import cv2
import random
import time

def get_screen():
    #截屏口令
    cmd_get = 'adb shell screencap -p /sdcard/screen_img.png'
    #发送图片口令
    cmd_send = 'adb pull sdcard/screen_img.png F:\yys'
    #截屏和发送操作
    os.system(cmd_get)
    os.system(cmd_send)
    img = cv2.imread('F:\yys\screen_img.png',0)
    return img

def matchEnd(img1, template):
    """img1代表待匹配图像, img2代表模板"""
    res = cv2.matchTemplate(img1,template,cv2.TM_CCOEFF_NORMED)
    print(res.max())
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    left_top = max_loc  # 左上角
    print(left_top,'\n')

def match(img1, template):
    """img1代表待匹配图像, img2代表模板"""
    res = cv2.matchTemplate(img1,template,cv2.TM_CCOEFF_NORMED)

    maxres = res.max()

    return maxres

def get_randxy(x, y):
    """产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
    xc = random.randint(x[0], x[1])
    yc = random.randint(y[0], y[1])

    return xc,yc

def get_randtime(a, b):
    """产生a,b间的随机时间延迟"""
    time.sleep(random.uniform(a, b))

def click(x, y):
    """输入两个二维列表，表示要点击的位置的x坐标，y坐标"""
    cmd_click = 'adb shell input tap {} {}'.format(x, y)
    os.system(cmd_click)