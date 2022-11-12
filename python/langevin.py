'''
Modelling Langevin Motion
returns trajectories of x(t) for single realization of white noise u(t).

T   temperature (Kelvin)
a   particle radius (um)
m   particle mass ()
N   number of time steps
dt  time step interval
D   diffusion coefficient
vi  initial particle velocity
'''

import numpy as npy
import numpy.random as nrand
import scipy.linalg as lin
import matplotlib.pyplot as plt

def viscosity(T):
    return T

def langevin(T, a, m, dt, N, D, vi):
    a = a*1E-6              # particle radius (um)
    h = 6.6262E-34          # Planck's constant (Js)
    kb = 1.3806503e-23      # Boltzmann constant (J/K)
    eta = viscosity(T)*1E-6 # return viscosity of water (uPa.s)

    t = npy.linspace(dt,dt*N,N) # [h, 2h, 3h, 4h] timesteps
    v = npy.zeros(1,N)      # container of particle velocity values
    v[1] = vi               # set initial particle velocity
    alpha = 6*npy.pi*eta*a  # Stokes friction coefficient
    qconst = -alpha/m       # drift term coefficient
    gconst = 1.0/m          # diffusion term coefficient
    sigma = npy.sqrt(2*kb*T*alpha)  # noise strength

    k = gconst*npy.sqrt(dt)*sigma
    k2 = dt*qconst

    for i in range(len(v)-1):
        v[i+1] = v[i] + k2*v[i]+ k*nrand.random()

    # get the x trajectories from v datapoints
    dx = npy.multiply(v,dt)
    vi = v(len(v))

    return dx,vi

