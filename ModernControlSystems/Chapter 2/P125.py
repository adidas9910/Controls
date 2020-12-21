# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-14
import scipy.signal as sig
import numpy as np
import control.matlab as cm
import matplotlib.pyplot as plt

ng1 = np.array([1])
dg1 = np.array([1, 10])
sysg1 = cm.tf(ng1, dg1)
ng2 = np.array([1])
dg2 = np.array([1, 1])
sysg2 = cm.tf(ng2, dg2)
ng3 = np.array([1, 0, 1])
dg3 = np.array([1, 4, 4])
sysg3 = cm.tf(ng3, dg3)
ng4 = np.array([1, 1])
dg4 = np.array([1, 6])
sysg4 = cm.tf(ng4, dg4)

nh1 = np.array([1, 1])
dh1 = np.array([1, 2])
sysh1 = cm.tf(nh1, dh1)
nh2 = np.array([2])
dh2 = np.array([1])
sysh2 = cm.tf(nh2, dh2)
nh3 = np.array([1])
dh3 = np.array([1])
sysh3 = cm.tf(nh3, dh3)

sys1 = sysh2/sysg4
sys2 = cm.series(sysg3, sysg4)
sys3 = cm.feedback(sys2, sysh1, +1)
sys4 = cm.series(sysg2, sys3)
sys5 = cm.feedback(sys4, sys1)
sys6 = cm.series(sysg1, sys5)
sys = cm.feedback(sys6, sysh3)

print(sys)
stepinfo = cm.stepinfo(sys)
print(stepinfo)
stepsys2, stepsys1= cm.step(sys)
plt.plot(stepsys1, stepsys2)
plt.show()



#sys = control.matlab.feedback(sys3, control.tf(np.array([1]),np.array([1])), -1)
#print(sys)

