# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-14
# Page 207

import numpy as np
import control.matlab as cm
import matplotlib.pyplot as plt
import scipy.linalg as splg

A = np.array([[0,-2],[1,-3]])
B = np.array([[2],[0]])
C = np.array([1,0])
D = np.array([0])
sys = cm.ss(A,B,C,D)
x0 = np.array([1,1])
t = np.arange(0,1,0.01)
u = 0*t
y, T, x = cm.lsim(sys, u, t, x0)

plt.figure(1)
plt.subplot(121)
plt.plot(T,x[:,0])
plt.xlabel('Time (s)')
plt.ylabel('x_1')
plt.grid()
plt.subplot(122)
plt.plot(T,x[:,1])
plt.xlabel('Time (s)')
plt.ylabel('x_2')
plt.grid()
plt.show()

