#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import numpy
import sklearn.cluster
import pygame, sys
from pygame.locals import *

positions = numpy.random.randint(9, 400, size=(30, 2))

positions_norms = numpy.sum(positions  ** 2, axis=1)
S = - positions_norms[:, numpy.newaxis] - positions_norms[numpy.newaxis, :] + 2 * numpy.dot(positions, positions.T)
