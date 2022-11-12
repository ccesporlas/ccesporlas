import numpy as npy
import numpy.matlib as nmat
import scipy.linalg as lin
import matplotlib.pyplot as plt

def Q1(j,k):
    q = npy.sqrt(j+k+1)/2
    return q

def q(n):
    q = npy.zeros((n,n))
    j = nmat.repmat(npy.arange(n),n,1)
    i = npy.transpose(j)
    q = Q1(i,j)
    for i in range(n):
        for j in range(n):
            if abs(i-j) != 1:
                q[i,j] = 0
    return q

def H0(n):
    h = npy.zeros((n,n),dtype=float)
    for i in range(n):
        h[i,i] = i+0.5
    return h
    #return scipy.diagflat(scipy.arange(n)+0.5)

def H(l,n):
    qn = npy.matrix(q(n))
    h = H0(n)+l*qn*qn*qn*qn
    return h

def energy(l,n):
    h = H(l,n)
    energy = lin.eig(h,left=False,right=False)
    return energy

fig, (ax1,ax2,ax3) = plt.subplots(1,3) #figsize=(9,7),dpi=1000
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.95,top=0.95,wspace=0.4,hspace=0.4)

# Figure 1
n = 4
l = npy.linspace(0,1,20)
j = 0
e = npy.zeros((20,n))
for lmb in l:
    e[j,:] = energy(lmb,n)
    j += 1
    se = npy.sort(e)
for j in range(n):
    ax1.plot(l,se[:,j])

# Figure 2
nall = 20
lmb = 0.1
j = 0
smallestE = npy.zeros(nall-7)
for n in range(7,nall):
    e = energy(lmb,n)
    se = npy.sort(e)
    smallestE[j] = se[0]
    j += 1
ax2.plot(smallestE)

# Figure 3
n = 20
l = npy.linspace(0,1,20)
j = 0
e = npy.zeros((20,n))

for lmb in l:
    e[j,:] = energy(lmb,n)
    j += 1
    se = npy.sort(e)
for j in range(5):
    ax3.plot(l,se[:,j])

plt.show()