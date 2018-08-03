#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame, sys
from pygame.locals import *
import numpy

pygame.init()
# surfarray handles the confersion between Surface and NumPy arrays
# array2d copies pixels into a 2-d array
pixels = pygame.surfarray.array2d(img)

X = pixels.shape[0] * 7
Y = pixels.shape[1] * 7
screen = pygame.display.set_mode((X, Y))
