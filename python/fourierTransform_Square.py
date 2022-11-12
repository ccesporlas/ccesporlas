# Fourier Transform - square wave
import numpy as npy, numpy.fft as nfft
import matplotlib.pyplot as plt

# rectangular pulse
def f(t,tau):
    return 0.5*(npy.sign(tau+t) + npy.sign(tau-t))

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
    fapprox = npy.dot(ftilde,coeff)/N #scipy.sqrt(N)
    return fapprox

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1) #figsize=(9,7),dpi=1000
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.95,top=0.95,wspace=0.4,hspace=0.4)

# Plot 1,2
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

ax1.set_title('Square Wave')
ax1.plot(t,y,'r-',label='square wave')
ax1.legend()
ax1.grid('true')
ax2.plot(t,ftilde,'g-',label='fft')
ax2.legend()
ax2.grid('true')
ax3.plot(textend,z,'bo-',markersize=2,linewidth=0.5,label='approximation')
ax3.legend()
ax3.grid('true')

# Plot 2 - Square Wave
## note: At the output the amplitude  b_s is multiplied by the Vo(w_s), w/c we
##obtained from the ... HOWEVER THIS is valid only for s= 1,...N/2(lower freqs)
## Higher freq result in an inaccurate approxn for Vi(t) as shown in Sec 1.3.
## Thus shift the higher freqs to low negative ones, using b_s=b_s-N, before
##transforming  Vo(w_s)

x = npy.linspace(-10,10,N)
sqwv = 1-2*npy.mod(npy.floor(x-1/N),2)
ax4.plot(x,sqwv,label='square wave')
ax4.plot(x,nfft.fft(sqwv),label='fft')
ax4.plot(x,nfft.ifft(sqwv),label='inverse fft')
ax4.axis([-10,10,-30,30])
ax4.legend()
ax4.grid('true')

plt.show()