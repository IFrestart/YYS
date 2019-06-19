# -*- coding:UTF-8 -*-
import cacl as yf
import cv2
from config import Settings
import time
import random

def beginbaigui():
    t_start = cv2.imread('F:\yys\\baigui.png', 0)
    t_start1 = cv2.imread('F:\yys\\baigui1.png', 0)
    t_end = cv2.imread('F:\yys\\baiguiend.png', 0)
    t_join = cv2.imread('F:\yys\\baiguijoin.png', 0)
    t_friend = cv2.imread('F:\yys\\friend.png', 0)

    return t_start, t_start1,t_end, t_join,t_friend

def yuhun():
    t_start = cv2.imread('F:\yys\\yuhunStart.png', 0)
    t_end = cv2.imread('F:\yys\\yuhunEnd.png', 0)
    t_win = cv2.imread('F:\yys\\yuhunWin.png', 0)
    return t_start,t_end,t_win

def yeyuan():
    t_start = cv2.imread('F:\yys\\yeyuan.png', 0)
    t_end = cv2.imread('F:\yys\\yuhunEnd.png', 0)
    return t_start, t_end,

def yeyuanStart(tmp):
    settings = Settings()
    i = 0
    print("yuhunSTart")
    matching = match(tmp)
    if matching == 1:
        baiguiSelect(settings.start_x, settings.start_y)
        print ("select")
        yf.get_randtime(1, 2)
        matching = match(tmp)
        if matching == 1:
            print("xunhuan")
            yuhunStart(tmp)

def yeyuanEnd(end):
    settings = Settings()
    i = 0
    j = 0
    matching = match(end)
    if matching == 1:
        baiguiSelect(settings.yuhunEnd_x, settings.yuhunEnd_y)
        yf.get_randtime(0, 2)
        j=1
    return j

def yuhunStart(tmp):
    settings = Settings()
    i=0
    print("yuhunSTart")
    while(i<3):
        matching = match(tmp)
        if matching == 1:
            baiguiSelect(settings.yuhunStart_x,settings.yuhunStart_y)
            yf.get_randtime(1, 2)
            matching = match(tmp)
            if matching ==0:
                break
        i+=1

def yuhunEnd(tmp,win):
    settings = Settings()
    i = 0
    j = 0
    matching = match(win)
    if matching == 1:
        baiguiSelect(settings.yuhunStart_x, settings.yuhunStart_y)
        yf.get_randtime(1, 2)
        while(1):
            matching = match(tmp)
            if matching == 1:
                print("点击结束")
                baiguiSelect(settings.yuhunEnd_x, settings.yuhunEnd_y)
            else:
                j=1
                break

        yf.get_randtime(0, 2)

    return j

def baiguiSelect(x,y):
    sx, sy = yf.get_randxy(x,y)
    yf.click(sx, sy)

def baiguiInto(tmp,friend,friendNum):
    settings = Settings()
    i = 0
    judge = 0
    while(i<3):
        #初始界面
        baiguiSelect(settings.baigui_sx,settings.baigui_sy)
        matching = match(tmp)
        if matching == 1:
            if friendNum == 1:
                #点击添加好友
                baiguiSelect(settings.baiguiFriend_x,settings.baiguiFriend_y)
                matching = match(friend)
                if matching == 1:
                    #点击第一个好友
                    if (judge == 0):
                        baiguiSelect(settings.baiguiFS_x,settings.baiguiFS_y)
                        print("点击第一个好友")
                    else:
                        #点击第二个好友
                        baiguiSelect(settings.baiguiFS1_x, settings.baiguiFS_y)
                        print("点击第二个好友")
                    yf.get_randtime(1, 2)
                    matching = match(friend)
                    if matching == 1:
                        if judge == 0:
                            judge = 1
                            continue
                        else:
                            baiguiSelect(settings.baigui_sx, settings.baigui_sy)
                            friendNum = 0
                    else:
                        baiguiSelect(settings.baigui_x, settings.baigui_y)
                        yf.get_randtime(1, 2)
                        matching = match(tmp)
                        if matching == 0:
                            break;
                        else:
                            if judge == 0:
                                judge = 1
                            else:
                                friendNum = 0
                                baiguiSelect(settings.baiguiDelete_x, settings.baiguiDelete_y)
            else:
                baiguiSelect(settings.baigui_x, settings.baigui_y)
                yf.get_randtime(1, 2)
                matching = match(tmp)
                if matching == 0:
                    break;
        i += 1
    yf.get_randtime(1, 2)
    return friendNum

def baiguiStart(tmp):
    settings = Settings()
    i=0
    while(i<5):
        matching = match(tmp)
        #百鬼开始界面匹配
        if matching == 1:
            cacl = random.randint(1, 3)
            if cacl == 1:
                caclx = settings.baigui_x1

            if cacl == 2:
                caclx = settings.baigui_x2

            if cacl == 3:
                caclx = settings.baigui_x3

            baiguiSelect(caclx, settings.baigui1_y)
            yf.get_randtime(1, 2)
            baiguiSelect(settings.baiguiStart_x,settings.baiguiStart_y)
            yf.get_randtime(2, 3)
            matching = match(tmp)
            if matching == 1:
                baiguiStart(tmp)
            break
        i+=1
        print("baiguiStart")

def baiguiJoin(tmp):
    settings = Settings()
    matching = match(tmp)
    print('百鬼砸豆子匹配',matching)
    #百鬼砸豆子界面
    baiguiStep = 4
    if matching == 1:
        i=1
        while(i<20):
            yf.get_randtime(0.3, 0.6)
            baiguiSelect(settings.baiguiAttack_x,settings.baiguiAttack_y)
            i+=1
        baiguiJoin(tmp)
    else:
        baiguiStep = 5
        yf.get_randtime(3,5)
        print("百鬼结束")

def baiguiEnd(start,end):
    settings = Settings()
    i=0
    while(i<3):
        matching = match(end)
        if matching == 1:
            baiguiSelect(settings.baiguiend_x,settings.baiguiend_y)
            yf.get_randtime(1, 2)
            break
        else:
            matching = match(start)
            if matching == 1:
                break
        i+=1
        yf.get_randtime(1, 2)

#匹配模块*
#检测模板，
def match(t):
    sd = 0
    match = 0
    while(sd<3):
        img1 = yf.get_screen()
        res = yf.match(img1, t)
        print(res,'\n')
        if res > 0.80:
            match = 1;
            break;
        sd+=1
        yf.get_randtime(0.8, 1.3)
    return match

