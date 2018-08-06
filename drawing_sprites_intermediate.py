#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition

import os, pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except(pygame.error, message):
        print("Cannot load image: ", name)

    image = image.convert()

    return image, image.get_rect()

class Head(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('head.jpg', -1)
        screen = pygame.display.get_surface()
        self.STEP = 9
        self.MARGIN = 12
        self.xstep = self.STEP
        self.ystep = 0
        self.dizzy = 0
        self.direction = 'right'

def update(self):
    pass
