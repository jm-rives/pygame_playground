#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
import pygame, sys
from pygame.locals import *
import numpy

clock = pygame.time.Clock()

img = pygame.image.load('head.jpg')

steps = numpy.linspace(20, 260, 40).astype(int)
right = numpy.zeros((2, len(steps)))
down = numpy.zeros((2, len(steps)))
left = numpy.zeros((2, len(steps)))
up = numpy.zeros((2, len(steps)))

right[0] = steps
right[1] = 20
down[0] = 360
down[1] = steps
left[0] = steps[::-1]
left[1] = 360
up[0] = 20
up[1] = steps[::-1]

pos = numpy.concatenate((right.T, down.T, up.T))
