'''
pygame.draw命令操作
'''
# _*_coding:utf-8_*_

import pygame
from pygame.locals import *
import sys
from random import *
from math import  pi

pygame.init()
screen = pygame.display.set_mode((480,852),0,32)

#
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    #按任意键回复到原始位置
    if event.type == KEYDOWN:
        points=[]
        screen.fill((255,255,255))
    if event.type ==MOUSEBUTTONDOWN:
        screen.fill((255,255,255))
    #画出随机矩形
    rc = (randint(0,255),randint(0,255),randint(0,255))
    rp = (randint(0,480),randint(0,852)) #rp为矩形左上角的位置
    rs = (479-randint(rp[0],480),851-randint(0,852))#rs为矩形的长和宽
    pygame.draw.rect(screen,rc,Rect(rs,rs))
    #画出随机圆形
    rr = randint(0,200) #圆的半径
    pygame.draw.circle(screen,rc,rp,rr)
    #根据点击的位置画出弧线
    x,y=pygame.mouse.get_pos()
    points.append((x,y))
    angle = (x/480)*2*pi
    #pygame.draw.arc(surface,color,rect(pos,dim),start_angle,stop_angle,width)
    pygame.draw.arc(screen,(0,0,0),(0,0,480,852),0,angle,3)
    #根据点击位置的椭圆
    pygame.draw.ellipse(screen,(255,0,0),(0,0,x,y))
    #连线
    pygame.draw.line(screen,(0,0,0),(0,0),(x,y))

    pygame.display.update()
