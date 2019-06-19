# -*- coding:UTF-8 -*-
import attack as yf2
from config import Settings
import  cacl as ca
import threading
import os
from multiprocessing import Process
import  random
import time
#百鬼
def baigui():
    y_settings = Settings()
    t_start, t_start1,t_end ,t_join,t_friend= yf2.beginbaigui()
    friendNum = 1
    i=1
    while(1):
        print('开始第',i,'次百鬼')
        #百鬼进入匹配
        frinendNum = yf2.baiguiInto(t_start,t_friend,friendNum)
        #百鬼选择式神开始
        yf2.baiguiStart(t_start1)
        #百鬼开始砸碎片
        yf2.baiguiJoin(t_join)
        #结束
        yf2.baiguiEnd(t_start,t_end)
        ca.get_randtime(1,3)
        i += 1

#组队御魂
def zyuhun():
    y_settings = Settings()
    t_start, t_end,t_win= yf2.yuhun()
    while(1):
        j = 0
        #如果是队长则消掉注释
        #yf2.yuhunStart(t_start)
        while(j==0):
            ca.get_randtime(3, 5)
            j = yf2.yuhunEnd(t_end,t_win)
        ca.get_randtime(3,5)

#业原火
def yeyuan():
    y_settings = Settings()
    t_start, t_end = yf2.yeyuan()
    while (1):
        j = 0
        yf2.yeyuanStart(t_start)
        while (j == 0):
            ca.get_randtime(3, 5)
            j = yf2.yeyuanEnd(t_end)
        ca.get_randtime(3, 5)

if __name__ == '__main__':
    baigui()