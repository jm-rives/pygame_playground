#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# was returning error but I had not downloaded numpy
# still returning error, had to install numpy via https://stackoverflow.com/questions/17443354/install-numpy-on-python3-3-install-pip-for-python3
import numpy

colors = numpy.random.randint(0, 255, size=(4, 3))

WHITE = (255, 255, 255) # QUESTION? Would hex codes werk?
