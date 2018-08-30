import sys
print(sys.path)

"""Thankyou so much for the help, after playing around with the function
    more this morning and looking at a tutorial on numpy broadcasting I
    think i mostly understand it.
Turns out that each element in the X, Y, Z array corresponds with eachother
    to form one point (for example (X[0][1], Y[0][1], Z[0][1]) is a point
    plotted on the grid). The order and shape of the 2d array dictate how
    the mesh is constructed on the graph. Still don't exactly understand
    how the mesh construction happens, but the most 'sane' results occur
    via the output of numpy.meshgrid, where every element of either a mesh
    or column is equal, and increasing over the matrix. (Eg. [1,2,3],[1,2,3])
Also turns out that the reason the function accepts so many inputs is
    because of the call to numpy.broadcast at the start, which is
    similar to numpy.meshgrid for two inputs.
Just writing this out here to help set it in my mind. Thanks again for the help"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

#X = [[1, 2, 3, 4]]
#Y = [[-1, 5, 8, 2],[-2, -5, 6, 7],[-3, 1, 2, 6]]
#Z = [[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14]]

#X = [[1, 2, 3, 4, 1, 2], [3, 4, 1, 2, 3, 4]]
#Y = [[-1, 5, 8, 2, -2, -5], [6, 7, -3, 1, 2, 6]]
#Z = [[1, 2, 3, 4, 6, 7], [8, 9, 11, 12, 13, 14]]

#X = [[1, 2, 3], [4, 1, 2], [3, 4, 1], [2, 3, 4]]
#Y = [[-1, 5, 8], [2,-2, -5], [6, 7,-3], [1, 2, 6]]
#Z = [[1, 2, 3], [4, 6, 7], [8, 9, 11], [12, 13, 14]]

X = [[4, 2, 3, 1]]
Y = [[2, 5, 8, -1],[7, -5, 6, -2],[6, 1, 2, -3]]
Z = [[4, 2, 3, 1], [9, 7, 8, 6], [14, 12, 13, 11]]

ax.plot_surface(np.array(X), np.array(Y), np.array(Z))
plt.show()
