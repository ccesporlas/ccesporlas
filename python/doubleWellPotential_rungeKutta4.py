# Particle behavior in a double-well potential
# 4th order Runge-Kutta Method
# A particle of mass m moves in a 1D double-well potential and is
# subject to an additional frictional force proportional to its velocity.
# Equation of motion for position x(t) as a function of time t
#   m*x'' = mu*x' + a*x - b*x^3
# where mu,a,b are positive constants
import numpy as npy, matplotlib.pyplot as plt

'''
# Sample 2D system
def derivs6(x,t):
    d1 =  x[0] + 2*x[1]
    d2 =  -3*x[0] + 4*x[1]
    return (d1, d2)
dt = 0.0005
t = arange(0.0, 2.0, dt)
y0 = (1,2)
yout = rk4(derivs6, y0, t)

# Sample 1D system
def derivs(x,t):
    return -alpha*x + exp(-t)
alpha = 2
y0 = 1
yout = rk4(derivs, y0, t)
'''

def derivs6(x,t):
    d1 =  x[1]
    d2 =  -0.1*x[1] + x[0] - x[0]*x[0]*x[0]
    return (d1,d2)

def rk4(derivs, y0, t):
    """
    Integrate 1D or ND system of ODEs from initial state y0 at sample
    times t.  derivs returns the derivative of the system and has the
    signature
    """
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

t = npy.arange(0.0,100.0,0.05)

for i in npy.linspace(-2.5,2.5,30):
    for j in npy.linspace(-2.5,2.5,30):
        yout = rk4(derivs6, [i,j], t)
        x = yout[0:,0]
        y = yout[0:,1]

        l = len(x)
        if (-1.5 < x[l-1] < -0.5):
            if (-0.5 < y[l-1] < 0.5):
                plt.plot(x,y,'go',markersize=0.8)
                plt.title('Basin of Attraction for the Double-Well Potential as x(infinity)=-1')
                plt.xlabel('initial positions, x(0)')
                plt.ylabel('initial velocities, xdot(0)')
                plt.axis([-2,2,-2,2])

plt.show()