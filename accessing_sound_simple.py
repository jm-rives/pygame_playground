#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition
import pygame
from pygame.locals import *
import urllib2
import time

WAV_FILE = 'smashingbaby.wav'

def play:
    audio = pygame.mixer.Sound(WAV_FILE)
    audio.play(-1)
    TIMEOUT = 1
    pygame.time.delay(TIMEOUT * 1000)
    audio.stop()

pygame.init()
