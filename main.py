#!/usr/bin/python

import pygame
from pygame.locals import *

pygame.init()
# Ouvre une fenetre de 800 sur 60
fenetre = pygame.display.set_mode((800, 600))
ouvert = True
while ouvert:
    for event in pygame.event.get():
        if event.type == QUIT:
            ouvert = False
