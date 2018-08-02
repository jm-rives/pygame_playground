#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame, sys
from pygame.local import *
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

matplotlib.use("Agg")

fig = plt.figure(figsize=[3, 3])
