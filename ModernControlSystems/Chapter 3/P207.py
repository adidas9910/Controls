# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-14
# Page 207

import numpy as np
import control.matlab as cm
import matplotlib.pyplot as plt

num = np.array([2, 8, 6])
den = np.array([1,8,16,6])
sys_tf = cm.tf(num, den)
sys_ss = cm.ss(sys_tf)
print(sys_ss)

stepinfo = cm.stepinfo(sys_ss)
print(stepinfo)
stepsys2, stepsys1= cm.step(sys_ss)
plt.figure(1)
plt.plot(stepsys1, stepsys2)
plt.grid()
#plt.show()

plt.figure(2)
t = np.arange(0,3,step=0.005)
y, t = cm.step(sys_ss, t)
plt.plot(t, y)
plt.grid()
plt.show()

