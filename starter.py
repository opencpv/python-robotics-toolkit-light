import rot2d
import homogenous
from math import pi,radians
import numpy as np
from math import cos,sin

rotation_mat = rot2d.rotx(pi/2)
mat = homogenous.se2(1,2,radians(30))
print(sin(0.5235))