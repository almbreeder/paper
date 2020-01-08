import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((480,852),0,32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    rand_col = (randint(0,255),randint(0,255),randint(0,255))

    #screen.lock() #lock会将surface锁住，以保证不会有其它进程来干扰
    for _ in range(100):
        rand_pos = (randint(0,480),randint(0,852))
        screen.set_at(rand_pos,rand_col)
    #screen.unlock()#与lock成对出现

    pygame.display.update()