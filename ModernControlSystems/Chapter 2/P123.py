# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-13
import scipy.signal as sig
import numpy as np
import control
import control.matlab
import matplotlib.pyplot as plt

numg = np.array([1])
deng = np.array([500, 0, 0])
sys1 = control.tf(numg, deng)
print(sys1)
numc = np.array([1, 1])
denc = np.array([1, 2])
sys2 = control.tf(numc, denc)
print(sys2)

sys3 = control.matlab.series(sys1, sys2)

print(sys3)

sys = control.matlab.feedback(sys3, control.tf(np.array([1]),np.array([1])), -1)
print(sys)

