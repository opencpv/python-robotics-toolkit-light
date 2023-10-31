from math import cos,sin
import numpy as np


def rotx(theta) :
    row1 = [cos(theta) ,sin(theta) ]
    row2 = [-sin(theta),cos(theta)]
    return np.array([row1,row2])
