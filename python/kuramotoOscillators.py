# Synchronization of Kuramoto Oscillators
# 4th order Runge-Kutta Method

import numpy as npy, matplotlib.pyplot as plt

def derivs(x,t,r,psi):
    return  w + K*r*npy.sin(npy.mod(psi-x[0],2*pi))

pi = npy.pi
N = 1000 #number of oscillators
nt = 10000 #number of time steps

w = npy.random.normal(0.,1,N) # natural frequency of oscillators

#K = npy.linspace(0.0,20.0,40)
K = 0.5

t = npy.linspace(0.0,10000.0,nt)

theta = npy.zeros([nt,N],npy.float_) #phase array[timestep,Nth oscillator]
theta[0,:] = npy.random.uniform(0,2*pi,N) #initial phase

psi = npy.zeros(nt,npy.float_) #mean phase array
psi[0] = npy.mean(theta[0,:]) #initial mean phase

rt = npy.zeros(nt,npy.float_)
rx0 = npy.mean( npy.cos( npy.mod(theta[0,:],2*pi) ) ) #xcomponent of r init
ry0 = npy.mean( npy.sin( npy.mod(theta[0,:],2*pi) ) ) #ycomponent of r init
rt[0] = npy.sqrt( rx0**2 + ry0**2 )

for i in npy.arange(nt-1):

    thist = t[i]
    dt = t[i+1] - thist
    dt2 = dt/2.0

    y0 = theta[i,:]
    r0 = rt[i]
    psi0 = psi[i]

    k1 = npy.asarray(derivs(y0, thist, r0, psi0))
    k2 = npy.asarray(derivs(y0 + dt2*k1, thist+dt2, r0, psi0))
    k3 = npy.asarray(derivs(y0 + dt2*k2, thist+dt2, r0, psi0))
    k4 = npy.asarray(derivs(y0 + dt*k3, thist+dt, r0, psi0))

    theta[i+1,:] = y0 + dt/6.0*(k1 + 2*k2 + 2*k3 + k4)

    psi[i+1] = npy.mean(theta[i+1,:])

    rx = npy.mean( npy.cos( npy.mod(theta[i+1,:],2*pi) ) ) #xcomponent
    ry = npy.mean( npy.sin( npy.mod(theta[i+1,:],2*pi) ) ) #ycomponent
    rt[i+1] = npy.sqrt( rx0**2 + ry0**2 )
