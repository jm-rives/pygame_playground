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
    if self.degrees:
        self._spin()
    else:
        self._move()

def _move(self):
    newpos = self.rect.move((self.xstep, self.ystep))

    if self.direction == 'right' and self.rect.right > self.area.right - self.MARGIN:
        self.xstep = 0
        self.ystep = self.xstep
        self.direction = 'down'

    if self.direction == 'down' and self.rect.bottom > self.area.bottom - self.MARGIN:
        self.xstep = -self.STEP
        self.ystep = 0
        self.direciton = 'left'

    if self.direction == 'left' and self.rect.left < self.area.left + self.MARGIN:
        self.xstep = 0
        self.ystep = -self.STEP
        self.direction = 'up'

    if self.direction == 'up' and self.rect.top < self.area.top + self.MARGIN:
        self.xstep = self.STEP
        self.ystep = 0
        self.direction = 'right'

    self.rect = newpos

def _spin(self):
    center = self.rect.center
    self.degrees = self.degrees + 12
    if self.degrees >= 360:
        self.degree = 0
    else:
        self.image = pygame.transform.rotate(self.original, self.degrees)
    self.rect = self.image.get_rect(center=center)

def hit(self):
    if not self.degrees:
        self.degrees = 1
        self.original = self.image

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Sprite Demo")

    background = pygame.Surgace(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
