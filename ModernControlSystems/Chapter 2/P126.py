# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-14
import scipy.signal as sig
import numpy as np
import control.matlab as cm
import matplotlib.pyplot as plt

num = np.array([1, 4, 6, 6, 5, 2])
den = np.array([12,205,1066,2517,3128,2196,712])
sys1 = cm.tf(num, den)
sys = cm.minreal(sys1)
print(sys)

num1 = np.array([10])
den1 = np.array([1, 1])
sys1 = cm.tf(num1, den1)

num2 = np.array([1])
den2 = np.array([2, 0.5])
sys2 = cm.tf(num2, den2)

num3 = np.array([540])
den3 = np.array([1])
sys3 = cm.tf(num3, den3)

num4 = np.array([0.1])
den4 = np.array([1])
sys4 = cm.tf(num4, den4)

sys5 = cm.series(sys1, sys2)
sys6 = cm.feedback(sys5, sys4)
sys7 = cm.series(sys3, sys6)
sys = cm.feedback(sys7,1,-1)

print(sys)
stepinfo = cm.stepinfo(sys)
print(stepinfo)
stepsys2, stepsys1= cm.step(sys)
plt.figure(1)
plt.plot(stepsys1, stepsys2)
plt.grid()
#plt.show()

# Page 127
plt.figure(2)
t = np.arange(0,3,step=0.005)
y, t = cm.step(sys, t)
plt.plot(t, y)
plt.grid()
plt.show()

