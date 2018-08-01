#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# was returning error but I had not downloaded numpy
# still returning error, had to install numpy via
# https://stackoverflow.com/questions/17443354/install-numpy-on-python3-3-install-pip-for-python3
import pygame, sys
from pygame.locals import *
import numpy

pygame.init()
screen = pygame.display.set_mode((400,400))

colors = numpy.random.randint(0, 255, size=(4, 3))

WHITE = (255, 255, 255) # QUESTION? Would hex codes werk?

# this should result in a surface that is white
screen.fill(WHITE)

# this should result in a ciricle being displayed in our screen
pygame.draw.circle(screen, colors[0], (200, 200), 25, 0)

# this should result in a line drawn to the screen
# takes start and end point, final parameter indicates line thickness
pygame.draw.line(screen, colors[1], (0, 0), (200, 200), 3)

# this should result in a rectangle being drawn to the surface
# required paramters are color, coordinates of upper left hand corner, and dimensions
pygame.draw.rect(screen, colors[2], (200, 9, 100, 100))

# this should result in an elilipse being drawn to the surface
pygame.draw.ellipse(screen, colors[3], (100, 300, 100, 50), 2)
