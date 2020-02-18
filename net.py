#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

y = np.array([0, 0, 1, 1]).T ## .T (transpose) convert this 1x4 matrix to a 4x1 matrix in order to match 
print y
plt.matshow(np.hstack((X,y)), fignum=10, cmap=plt.cm.gray)
plt.show()
