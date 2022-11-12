import numpy as npy
import matplotlib.pyplot as plt

# TODO: make a ssimple fun app... maybe

# R, r, T, and O may be modified as long as R>r
T = 1000 # may be modified
t = npy.linspace(0,T,T)
R = 6.0
r = 4.0
O = 5.0
x = []
y = []

for i in t:
    x.append((R+r)*npy.cos(i) - (r+O)*npy.cos(((R+r)/r)*i))
    y.append((R+r)*npy.sin(i) - (r+O)*npy.sin(((R+r)/r)*i))

plt.plot(x,y,'b-',linewidth=0.2)
plt.title('R=6,r=4,T=1000,O=5')
plt.axis('square')
plt.show()