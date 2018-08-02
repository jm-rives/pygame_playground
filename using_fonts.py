#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame, sys
from pygame.locals import *
import numpy

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

pos = numpy.concatenate((right.T, down.T, left.T, up.T))
i = 0

# create a font
font = pygame.font.Font('chunkfive.ttf', 32)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

while True:
    # Erase screen
    screen.fill((255, 255, 255))

    if i >= len(pos):
        i = 0

    screen.blit(img, pos[i])

    # displaying text in the center of the screen
    # updated to new syntax
    text = "{!s} {!s} {!s}".format(i, pos[i][0], pos[i][1])
    rendered = font.render(text, True, RED, BLUE)
    screen.blit(rendered, (150, 200))
    i += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)
