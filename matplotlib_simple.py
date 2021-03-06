#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame, sys
from pygame.locals import *
import numpy
import matplotlib
# Instance attribute specifies non-iteractive back-end and must be called before
# other matplotlibs
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


# creates a 3" x 3" figure
fig = plt.figure(figsize=[3, 3])
# creates a subplot
ax = fig.add_subplot(111)
# creates non-iteractive mode canvas
canvas = agg.FigureCanvasAgg(fig)

def plot(data):
    # function creates a plot using specified data
    ax.plot(data)
    # function that draws the canvas
    canvas.draw()
    # gets a renderer for the canvas
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
up = numpy.zeros((2, len(steps)))

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

while True:
    # Erase screen
    screen.fill((255, 255, 255))
    if i >= len(pos):
        i = 0
        surf = plot(history)

    screen.blit(img, pos[i])
    history = numpy.append(history, pos[i])
    screen.blit(surf, (100, 100))

    i += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)
