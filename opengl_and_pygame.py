#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# was returning error but I had not downloaded numpy
# still returning error, had to install numpy via
# https://stackoverflow.com/questions/17443354/install-numpy-on-python3-3-install-pip-for-python3

import pygame
from pygame.locals import *
import numpy

from OpenGl.Gl import *
from OpenGl.GLU import *

def display_openGl(w, h):
    pygame.display.set_mode((w, h), pygame.OPENGL|PYGAME.DOUBLEBUF)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUGGER_BIT|GL_DEPTH_BUFFER_BIT)
