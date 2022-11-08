# Modelling the convection in the atmosphere, Lorenz used a 2D fluid cell
# where it is heated at the bottom and cooled at the top,
# like the sun heats the earth's surface and the earth. His model is a
# simplification of the Navier-Stokes fluid equations, using a Fourier expansion
# in the x and z directions and neglecting higher-order terms.
# The two surfaces (top and bottom) have maintained temperatures
# such that their temperature difference is constant (Rayleigh-Benard cell).
# Convection will not be observed when the temperature difference is not very large.
# Buoyant forces will overcome viscosity when the temperature difference is large enough
# creating steady circulating currents or convection.
# #Determine the behaviour of a turbulent fluid system given different initial conditions

import numpy, scipy.integrate, matplotlib.pyplot as plt

#initialize a value for r
r = 28

#Lorenz Equations
def derivs6(x,t):
  d1 = -10*x[0] + 10*x[1]
  d2 = -x[0]*x[2] + r*x[0] - x[1]
  d3 = x[0]*x[1] - (8/3)*x[2]
  return (d1,d2,d3)

t = numpy.arange(0.0,100.0,0.005)
y0 = (1,1,1)

#get solutions of the Lorenz Equations
yout = scipy.integrate.odeint(derivs6,y0, t)

#empty array for Poincare Section
z20=[]

#Search and plot (X,Y) at plane Z = 20
for i in range(len(yout)):
  if (19.5<yout[i,2]<20.5):
    z20.append([yout[i,0],yout[i,1]])
z20 = numpy.array(z20)

plt.plot(z20[0:,0],z20[0:,1],'r.')

x = yout[0:,0]
y = yout[0:,1]
#Plot trajectory

plt.plot(x,y,'g-')
plt.title('Lorenz Convection Model')
plt.xlabel('Velocity of Cicular Motion')
plt.ylabel('Temperature Difference')
plt.show()