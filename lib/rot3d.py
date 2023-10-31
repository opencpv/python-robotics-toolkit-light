from math import cos,sin
import numpy as np

def rotx(theta) :
    row1 = [1 ,0, 0]
    row2 = [0, cos(theta) ,-sin(theta) ]
    row3 = [0 ,sin(theta),cos(theta)]
    return np.array([row1,row2,row3])
    
def roty(theta) :
    row1 = [cos(theta) ,0,sin(theta)]
    row2 = [0 ,1, 0]
    row3 = [-sin(theta),0,cos(theta)]
    return np.array([row1,row2,row3])

    
def rotz(theta) :
    row1 = [cos(theta) ,-sin(theta),0]
    row2 = [sin(theta),cos(theta),0]
    row3 = [0,0,1]
    return np.array([row1,row2,row3])
