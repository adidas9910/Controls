# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-02
import scipy.signal as sig
import numpy as np
import control
import matplotlib.pyplot as plt

num1 = np.array([6, 0, 1])
den1 = np.array([1, 3, 3, 1])
sysg = control.tf(num1, den1)
print(sysg)

p = control.pole(sysg)
print(p)

z = control.zero(sysg)
print(z)

p, z = control.pzmap(sysg)
print(p)
print(z)

n1 = np.array([1, 1])
n2 = np.array([1, 2])
d1 = np.array([1, 2j])
d2 = np.array([1, -2j])
d3 = np.array([1, 3])
numh = np.convolve(n1, n2)
print(numh)
denh = np.convolve(d1, np.convolve(d2, d3))
print(denh)
sysh = control.tf(numh, denh)
print(sysh)

sys = sysg/sysh
print(sys)

ps, zs = control.pzmap(sys)
print(ps)
print(zs)

plt.show()