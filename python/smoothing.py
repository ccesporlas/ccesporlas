# Smoothing Data

import scipy.special as special
import numpy as npy, numpy.fft as nfft, numpy.random as nrand
import matplotlib.pyplot as plt

N=256

# create noisy dataset
x = npy.linspace(0,10,N)
origdata = special.jn(1,x)
noise = 0.2*(nrand.rand(N)-0.5)
data = origdata + noise

# create the smoothing kernel
sigma = 0.3
x = npy.linspace(-5,5,N)
y = npy.exp(-x*x/(2*sigma*sigma))
index = round(N/2)
kernel = npy.concatenate((y[-index:],y[:index]))
kernel /= sum(kernel)  # normalize kernel

# perform smoothing
fdata = nfft.fft(data)
fkernel = nfft.fft(kernel)
smoothdata = nfft.ifft(fdata*fkernel)

# plotting routines
plt.plot(x,data,'r.',x,smoothdata,'b-',x,origdata,'g-')
plt.show()
