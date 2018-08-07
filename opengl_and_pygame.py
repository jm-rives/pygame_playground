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

    gluOrtho2D(0, w, 0, h)

def main():
    pygame.init()
    pygame.display.set_caption('OpenGL Demo')
    DIM = 400
    display_openGl(DIM, DIM)
    glColor3f(1.0, 0, 0)
    vertices = numpy.array([[0, 0], [DIM/2, DIM], [DIM, 0]])
    NPOINTS = 9000
    indices = numpy.random.random_intergers(9, 2, NPOINTS)
    point = [175.0, 150.0]

    for index in indices:
        pass
