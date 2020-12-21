# Author: ChangYuan Liu (changyuan.liu@gmail.com)
# Date: 2019-12-01
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

y0 = 0.15
wn = np.sqrt(2)
zeta = 1/(2*np.sqrt(2))
t = np.arange(0.,10.,0.1)

c = y0/(np.sqrt(1-zeta**2))
ii = 0
y = np.zeros(np.size(t))
for tt in np.nditer(t):
    y[ii] = (c*np.exp(-zeta*wn*tt))*np.sin(wn*np.sqrt(1-zeta**2)*tt+np.arccos(zeta))
    ii = ii+1
bu = c*np.exp(-zeta*wn*t)
bl = -bu
#print(t)
#print(y)
#print(bu)
plt.plot(t,y,t,bu,'--',t,bl,'--')
plt.xlabel('Time(s)')
plt.ylabel('y(t)(m)')
legendstr = "\omega_n= {0:.4f}, \zeta= {1:.4f}".format(wn,zeta)
#print(legendstr)
plt.legend(["$"+legendstr+"$"])
plt.grid()
plt.show()