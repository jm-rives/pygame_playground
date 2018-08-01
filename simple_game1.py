#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame, sys
from pygame.locals import *

# Initalize Pygame
pygame.init()

# calls the instance attribute of the display class set_mode
# that takes a tuple representing the width and height of
# creates a Surface
screen = pygame.display.set_mode((700, 500))

# sets the title of the display window
pygame.display.set_caption('Hello World!')

# game loop
while True:
    # sets the font, accepts to params font file (ttf or fon) (from cxv sep list) or 'None' and size.
    sys_font = pygame.font.SysFont("None", 40)
    # render params include string, anti-aliasing, rgb tuple
    rendered = sys_font.render('Hello World', 0, (0, 255, 255))
    # the function draws ON the Surface
    screen.blit(rendered, (100, 100))

    # this function cleans up resouces used by Pygame
    # should be called before every game exit is called.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # function refreshes the surface
    pygame.display.update()
