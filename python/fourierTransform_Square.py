# Fourier Transform - square wave
import numpy as npy, numpy.fft as nfft
import matplotlib.pyplot as plt

# rectangular pulse
def f(t,tau):
    return 0.5*(scipy.sign(tau+t)+scipy.sign(tau-t))

# continuous approximation
def fapprox(ftilde,t,T):
    N = ftilde.shape[0]
    Nextend = t.shape[0]
    s = npy.arange(N)
    stile = npy.transpose(npy.tile(s,(Nextend,1)))
    r = N*(t/T+0.5)
    rtile = npy.tile(r,(N,1))
    coeff = npy.exp(-2*npy.pi*1j*rtile*stile/N)
    # old version use scipy.repmat() instead
    fapprox=npy.dot(ftilde,coeff)/N #scipy.sqrt(N)
    return fapprox

T = 10
N = 256
Nextend=300
t = npy.linspace(-T/2,T/2-1.*T/N,N)
textend = npy.linspace(-T/2,T/2-1.*T/Nextend,Nextend)
tau = 1.

# discrete
ftilde = nfft.fft(f(t,tau))
y = nfft.ifft(ftilde)

z = fapprox(ftilde,textend,T)
plt.plot(textend,z,'ro-')
plt.show()