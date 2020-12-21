# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-01
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

p = np.array([1,3,0,4])
r = np.roots(p)
print(r)

p1 = np.poly(r)
print(p1)

p = np.array([3,2,1])
q = np.array([1,4])
n = np.convolve(p,q)
print(n)
v = np.polyval(n,-5)
print(v)
