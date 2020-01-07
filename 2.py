'''
在图片上加入字体
'''
# _*_coding:utf-8_*_
import pygame

from pygame.locals import *
import sys

pygame.init()

#创建窗口
screen = pygame.display.set_mode((480,852),0,32)
#设置标题
pygame.display.set_caption(u"飞机大战")
#创建字体
font = pygame.font.SysFont("arial",64)

#字体显示
text_surface = font.render("plane battle",True,(0,0,0))

x = -text_surface.get_width()
y=30

#背景图片
background = pygame.image.load('background.png')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    #显示背景图片
    screen.blit(background,(0,0))
    #文字移动
    x-=0.2
    if x < -text_surface.get_width():
        x=480 - text_surface.get_width()

    screen.blit(text_surface,(x,y))

    pygame.display.update()