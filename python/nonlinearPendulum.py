import numpy as npy
import scipy.special as special
import numpy.matlib as nmat
import numpy.fft as nfft
import matplotlib.pyplot as plt

def T(phi0):
    ''' Period of oscillation of a pendulum
        phi0: initial angle
        assumption: l/g = 1
    '''
    tmp = npy.sin(phi0/2.)
    out = 4*special.ellipk( tmp*tmp)
    return out

def sinepsi(t, phi0):
    '''sin(psi)'''
    tmp = npy.sin(phi0/2.)
    out = special.ellipj(t, tmp*tmp)
    return out[0]

def phinorm(tnorm, phi0):
    ''' Normalized phi(t) equal to phi(t)/phi0'''
    out = 2*npy.arcsin(npy.sin(phi0/2.)*sinepsi(tnorm*T(phi0),phi0))/phi0
    return out

def phidot(phi, emgl):
    ''' Positive square root of phidot
    negative square root also valid, emgl = E/mgl
    '''
    return 2*npy.sqrt((emgl+npy.cos(phi)))

def z(x,t):
    d1 = x[1]
    d2 = -r*x[1]-npy.sin(x[0])+a*npy.cos(w*t)
    return d1,d2

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2) #figsize=(9,7),dpi=1000
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.95,top=0.95,wspace=0.4,hspace=0.4)
pi = npy.pi

# Figure 1
# Plot T vs phi0
phi0_plot = npy.linspace(0,pi*(1-1./1000),1000)
T_plot = T(phi0_plot)
ax1.plot(phi0_plot/pi, T_plot/pi)
ax1.axis([0,1,0,10])
ax1.set_xlabel('phi0 (in units of pi)')
ax1.set_ylabel('T (in units of pi)')

# Figure 2
# Plot phi/phi0 vs t/T
N100 = 100
plot_tnorm = npy.linspace(0,1.,N100)
phi0_set = (pi*npy.array([1/10,1/4,1/2,4/5,99/100,999/1000])).tolist() # 6
plot_phinorm = npy.zeros((N100,len(phi0_set))) # (100,6)

for phi0 in phi0_set:
    plot_phinorm[:,phi0_set.index(phi0)] = phinorm(plot_tnorm,phi0)
    ax2.plot(plot_tnorm,phinorm(plot_tnorm,phi0))

plot_tnorm = nmat.repmat(plot_tnorm,len(phi0_set),1)
plot_tnorm = npy.transpose(plot_tnorm)
# plot_tnorm.shape --> check if the array is tiled correctly
ax2.set_xlabel('t/T')
ax2.set_ylabel('phi/phi0')

# Figure 3
# Display phase-space plot for Emgl = -1/2, 0, 1/2, 1, 3/2, 2
N100k = 100000
emgl_set = [-1./2, 0, 1./2, 1., 3./2, 2.] # 6
plot_phi = npy.zeros((N100k,len(emgl_set)))
plot_phidot = npy.zeros((N100k,len(emgl_set)))

for emgl in emgl_set:
    if float(emgl) >= 1. or float(emgl) < -1.:
        plot_phi = npy.linspace(-pi,pi,N100k)
    else:
        phi0 = npy.fabs(npy.arccos(-emgl))
        plot_phi = npy.linspace(-phi0,phi0,N100k)
    ax3.plot(plot_phi,phidot(plot_phi,emgl),'r-')
    ax3.plot(plot_phi,-phidot(plot_phi,emgl),'b-')

ax3.set_xlabel('phi')
ax3.set_ylabel('phidot')

# Figure 4
# Check for harmonics (signs of deviation from a pure sinusoidal oscillation)
phi0 = 999*pi/1000
N = 512
plot_tnorm = npy.linspace(0,1,N)
plot_phinorm = phinorm(plot_tnorm,phi0)
plot_fftphinorm = nfft.fft(plot_phinorm)
ax4.plot(abs(plot_fftphinorm[0:15]),'o')
ax4.set_xlabel('f')
ax4.set_ylabel('abs(FFT(phi(t)))')

# Extra
'''
t = npy.linspace(0,1000,1000000)
r = 0.25
a = 0.7
w = 2./3.
b = (0,1)
p = scipy.integrate.odeint(z, b, t)
plt.plot(p[:,0],p[:,1])
'''
plt.show()