#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition

# Pygame offers limited support for cutscenes (movie clips)
import pygame, sys
import pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Movie Demo')

def play():
    movie = pygame.movie.Movie('out.mpg')
    movie.play()
    TIMEOUT = 7
    pygame.time.delay(TIMEOUT * 1000)
    movie.stop()

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            play()
            pygame.quit()
            sys.exit()

    pygame.display.update()
