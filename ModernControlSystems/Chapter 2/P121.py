# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-02
import scipy.signal as sig
import numpy as np
import control
import matplotlib.pyplot as plt

numg = np.array([1])
deng = np.array([500, 0, 0])
sysg = control.tf(numg, deng)
print(sysg)
numh = np.array([1, 1])
denh = np.array([1, 2])
sysh = control.tf(numh, denh)
print(sysh)

sys = control.series(sysg, sysh)

print(sys)

