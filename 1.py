import pygame

from pygame.locals import *
import sys

backgroundImageName = 'background.png'
planeName = 'bomb.png'

#游戏初始化
pygame.init()

#创建一个窗口
screen = pygame.display.set_mode((480,852),0,32)
#设置窗口标题
pygame.display.set_caption("hello,world")

#加载图片
background = pygame.image.load(backgroundImageName)
plane = pygame.image.load(planeName)

#游戏主题
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出信号后退出游戏
            exit()

    #将背景图片画上
    screen.blit(background,(0,0))

    #获取鼠标位置
    x,y = pygame.mouse.get_pos()
    #计算光标左上角位置
    x -= plane.get_width() / 2
    y -= plane.get_height() /2

    #画上光标
    screen.blit(plane,(x,y))

    #刷新画面
    pygame.display.update()
