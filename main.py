# _*_coding:utf-8_*_

import os

import pygame
from pygame.locals import *
from music import *
import plane

path = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.mixer.init()

bg_size = 480, 852
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption(u"飞机大战")

background = pygame.image.load(os.path.join(path, "material/image/background.png"))

def main():
    running = True

    pygame.mixer_music.play(-1)
    clock = pygame.time.Clock()

    #生成我方飞机
    me = plane.MyPlane(bg_size)
    #切换飞机
    switchImage = True
    delay = 60

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # 检测用户的键盘操作
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()

        screen.blit(background, (0, 0))
        #绘制我方飞机
        if  (delay % 5):
            switchImage = not switchImage
        delay -= 1
        if delay==0:
            delay = 60

        if switchImage:
            screen.blit(me.image1, me.rect)
        else:
            screen.blit(me.image2, me.rect)

        clock.tick(60)

        pygame.display.update()


if __name__ == "__main__":
    main()
