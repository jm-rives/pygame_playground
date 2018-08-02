#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame, sys
from pygame.locals import *
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

matplotlib.use("Agg")

fig = plt.figure(figsize=[3, 3])
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)

def plot(data):
    ax.plot(data)
    canvas.draw()
    renderer = canvas.get_renderer()

    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    return pygame.image.fromstring(raw_data, size, "RGB")

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Animating Objects')
img = pygame.image.load('head.jpg')

steps = numpy.linspace(20, 360, 40).astype(int)
right = numpy.zeros((2, len(steps)))
down = numpy.zeros((2, len(steps)))
left = numpy.zeros((2, len(steps)))

right[0] = steps
right[1] = 20

down[0] = 360
down[1] = steps

left[0] = steps[::-1]
left[1] = 360

up[0] = 20
up[1] = steps[::-1]

pos = numpy.concatenate((right.T, down.T, left.T, up.T))
i = 0
history = numpy.array([])
surf = plot(history)
