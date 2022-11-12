import numpy.linalg as lin
import numpy as npy
import matplotlib.pyplot as plt

"""
Solve a system of linear equations
Version 0.1 by May Lim

vr + vo == 1
ir == ic + il
vr == ir r
vo == ic / I omega c
vo == I omega L il

solve for: vo, vr, ir, ic and il

This is equivalent to solving for vector x in: A*x == b.
"""

fig, (ax1,ax2) = plt.subplots(1,2)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.95,top=0.95,wspace=0.4,hspace=0.4)

# Part I.

N = 256
omegalist = npy.linspace(20000,43246,N)
Rlist = [100, 300, 900, 2700]
R = 2700
C = 1.E-6
L = 1.E-3

for R in Rlist:
    vomag = npy.zeros(N)
    vophase = npy.zeros(N)
    i = 0
    for omega in omegalist:
        A = npy.mat([[1, 1, 0, 0, 0],
            [0, 0, 1, -1, -1],
            [0, 1, -R, 0, 0],
            [1, 0, 0, -1/(1j*omega*C), 0],
            [1, 0, 0, 0, -1j*omega*L]])
        b = npy.mat('[1.;0;0;0;0]')
        x = lin.solve(A,b)
        vomag[i] = npy.abs(x[0])
        vophase[i] = npy.angle(x[0])
        i += 1

    ax1.plot(omegalist,vomag)
    ax1.set_xlabel('omega')
    ax1.set_ylabel('|Vo|')

    ax2.plot(omegalist,vophase)
    ax2.set_xlabel('omega')

# omegares=1./scipy.sqrt(L*C)

plt.show()