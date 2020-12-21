# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-02
import scipy.signal as sig
import numpy as np
import control
import matplotlib.pyplot as plt

num1 = np.array([1, 10])
den1 = np.array([1, 2, 1])
sys1 = control.tf(num1, den1)
print(sys1)

p = control.pole(sys1)
print(p)

z = control.zero(sys1)
print(z)

p, z = control.pzmap(sys1)
print(p)
print(z)
plt.show()