# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-02
import scipy.signal as sig
import numpy as np
import control
import matplotlib.pyplot as plt

num1 = np.array([10])
den1 = np.array([1,2,5])
sys1 = control.tf(num1, den1)
print(sys1)

num2 = np.array([1])
den2 = np.array([1,1])
sys2 = control.tf(num2,den2)
print(sys2)

sys = sys1+sys2
print(sys)
