import numpy as npy
import scipy, pylab

def derivs6(x,t):
    d1 =  x[1]
    d2 =  -0.1*x[1] + x[0] - x[0]*x[0]*x[0]
    return (d1,d2)

def rk4(derivs, y0, t):

    try: Ny = len(y0)
    except TypeError:
        yout = npy.zeros( (len(t),), npy.float_)
    else:
        yout = npy.zeros( (len(t), Ny), npy.float_)


    yout[0] = y0
    i = 0

    for i in npy.arange(len(t)-1):

        thist = t[i]
        dt = t[i+1] - thist
        dt2 = dt/2.0
        y0 = yout[i]

        k1 = npy.asarray(derivs(y0, thist))
        k2 = npy.asarray(derivs(y0 + dt2*k1, thist+dt2))
        k3 = npy.asarray(derivs(y0 + dt2*k2, thist+dt2))
        k4 = npy.asarray(derivs(y0 + dt*k3, thist+dt))
        yout[i+1] = y0 + dt/6.0*(k1 + 2*k2 + 2*k3 + k4)
    return yout


t=scipy.arange(0.0,100.0,0.1)

for i in scipy.linspace(-2.,2.,10):
    for j in scipy.linspace(-2.,2.,10):
        yout = rk4(derivs6, [i,j], t)
        x=yout[0:,0]
        y=yout[0:,1]

        l=len(x)
        
        if (-1.5 < x[l-1] < -0.5):
            if (-0.5 < y[l-1] < 0.5):
                pylab.plot(x,y)
pylab.show()

