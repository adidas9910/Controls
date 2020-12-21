# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-14
# Page 213

import numpy as np
import control.matlab as cm
import matplotlib.pyplot as plt
import scipy.linalg as splg

k = 10.0
M1 = 0.02
M2 = 0.0005
b1 = 410.0e-03
b2 = 4.1e-03
t = np.arange(0,1.5,0.001)
A = np.array([[0,0,1,0],[0,0,0,1],[-k/M1,k/M1,-b1/M1,0],[k/M2,-k/M2,0,-b2/M2]])
B = np.array([[0],[0],[1/M1],[0]])
C = np.array([0,0,0,1])
D = np.array([0])
sys = cm.ss(A,B,C,D)
y, t = cm.step(sys, t)
plt.figure(1)
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('y dot (m/s)')
plt.grid()
plt.show()

