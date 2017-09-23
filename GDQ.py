# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:30:28 2017

@author: XMKZ
"""

background_image_filename='stone.jpg'
moviee_image_filename='GDQ.png'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen=pygame.display.set_mode((700,800),0,32)
background=pygame.image.load(background_image_filename).convert()
moviee=pygame.image.load(moviee_image_filename)
x=0.
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(moviee,(x,100))
    x+=1.
    if x>700.:
        x=0.
    pygame.display.update()