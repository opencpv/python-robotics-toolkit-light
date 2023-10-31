import numpy as np
import rot2d


def se2(x, y, theta):
    rotation_mat = rot2d.rotx(theta)
    result = [[rotation_mat[0][0], rotation_mat[0][1], x], [
        rotation_mat[1][0], rotation_mat[1][1], y], [0, 0, 1]]
    return np.array(result)


def se3(x, y, theta):
    rotation_mat = rot2d.rotx(theta)
    result = [[rotation_mat[0][0], rotation_mat[0][1], rotation_mat[0][2], x],
              [rotation_mat[1][0], rotation_mat[1][1],
                  rotation_mat[1][0], rotation_mat[1][2], y],
              [rotation_mat[2][0], rotation_mat[2][1],
                  rotation_mat[2][0], rotation_mat[1][2], y],
              [0, 0, 1],
              ]
    return np.array(result)
