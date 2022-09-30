import numpy, matplotlib.pyplot as plt

def derivs6(x,t):
  d1 = x[1]
  d2 = -0.1*x[1] + x[0] - x[0]*x[0]*x[0]
  return (d1,d2)

def rk4(derivs, y0, t):
  try: Ny = len(y0)
  except TypeError:
    yout = numpy.zeros( (len(t),), numpy.float_)
  else:
    yout = numpy.zeros( (len(t), Ny), numpy.float_)

  yout[0] = y0
  i = 0

  for i in numpy.arange(len(t)-1):
    thist = t[i]
    dt = t[i+1] - thist
    dt2 = dt/2.0
    y0 = yout[i]

    k1 = numpy.asarray(derivs(y0, thist))
    k2 = numpy.asarray(derivs(y0 + dt2*k1, thist+dt2))
    k3 = numpy.asarray(derivs(y0 + dt2*k2, thist+dt2))
    k4 = numpy.asarray(derivs(y0 + dt*k3, thist+dt))
    yout[i+1] = y0 + dt/6.0*(k1 + 2*k2 + 2*k3 + k4)

  return yout

t = numpy.arange(0.0,100.0,0.05)

for i in numpy.linspace(-2.5,2.5,30):
  for j in numpy.linspace(-2.5,2.5,30):
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
        ## else:
        ## pylab.plot(x,y,'ro')
        ## pylab.axis([-2,2,-2,2])

plt.show()