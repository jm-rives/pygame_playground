#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
import pygame, sys
from pygame.locals import *

# Initalize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

while True:
    sys_font = pygame.font.SysFont("None", 19)
    rendered = sys_font.render('Hello World', 0, (0, 255, 255))
    screen.blit(rendered, (100, 100))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
