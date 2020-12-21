# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-14
# Page 207

import numpy as np
import control.matlab as cm
import matplotlib.pyplot as plt
import scipy.linalg as splg

A = np.array([[0,-2],[1,-3]])
dt = np.array([0.2])
print(A*dt)
Phi = splg.expm(A*dt)

print(Phi)


