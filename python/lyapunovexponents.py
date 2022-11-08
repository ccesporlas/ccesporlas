# Central Limit Behavior of Deterministic Dynamical Systems
# Logistic Equations
# 1. x_i+1 = 1 - a*(x_i)**2
# 2. x_i+1 = 4*(x_i)**3 - 3*x_i
# 3. x_i+1 = 1 - a* |x_i|**z

import numpy as npy, matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
#import cdf

def fn(r,x):
    return 1 - r*(x**2)                    #1
    #return r*x*(1.0-x) - (x**2)/(1+x**2)    #2
    #return r*x*(1.0-x)                     #3
    #return 4*r*x*(1.0-x)                   #4

def dfn(r,x):
    return 2*r*x                            #1
    #return r-2*r*x - (2*x)/(1+x**2)**2     #2
    #return r-2*r*x                         #3
    #return 4*r-8*r*x                       #4

def getSumOfIterates(r,n_init,n_iter):
    # r         logistic equation control parameter
    # n_init    number of initial values
    # n_iter    number of iterations
    # y         sum of iterates
    xi = npy.linspace(0.,1.,n_init)
    y = npy.zeros(n_init)

    for i in range(n_init):
        x = npy.zeros(n_iter)
        x[0] = xi[i]
        for j in range(n_iter):
            if j < n_iter-1:
                x[j+1] = fn(r,x[j])
        xav = npy.mean(x)
        y[i] = sum(x-xav)/npy.sqrt(n_iter)

    y = y/max(y)

    #store values in a file
    #f = open("raw", 'w')
    #for i in y:
    #    f.write("%s\n"%i)
    #cdf.CDF("raw", 2, "pdf")

    return y

def getHistPoints(iterates):
    counts, edges = npy.histogram(iterates,bins=50)
    centers = (edges[:-1] + edges[1:]) / 2
    return centers,counts

def gauss(x,a,mu,sigma):
    # x = bins from histogram data
    # a = 1/(sigma * npy.sqrt(2 * npy.pi))
    # mu = mean or expectation value
    # sigma = standard deviation
    return a* npy.exp(-(x-mu)**2 / (2*sigma**2))

def getFit(xdata,ydata):
    mu = npy.mean(ydata)
    sigma = npy.std(ydata)
    [aFit,muFit,sigmaFit], covariance = fit(gauss,xdata,ydata)
    return gauss(xdata,aFit,muFit,sigmaFit)

N = 2000
rrange = npy.linspace(0.1,2.0,N)

#Create arrays to store lyapunov exponents at each parameter value
lexp = []
rlexp = []

fig1, (ax1) = plt.subplots(1,1)

for r in rrange:
    #Set initial condition
    x_n = 0.65

    #Remove initial transient iterations
    for i in range(100):
        x_n = fn(r,x_n)

    #Bifurcation
    rlist = []
    xn = []

    for i in range(N):
        x_n = fn(r,x_n)
        rlist.append(r)
        xn.append(x_n)

    ax1.plot(rlist, xn, 'r.')

    #Estimate lyapunov exponents over N iterations
    l = 0.0
    for i in range(N):
        x_n = fn(r,x_n)
        l = l + npy.log(abs(dfn(r,x_n)))

    #Get average of lyapunov exponent per iteration
    l = l/float(N)
    lexp.append(l)
    rlexp.append(r)
    ax1.plot(rlexp,lexp,'g',linewidth=0.5)

ax1.hlines(0, min(rlexp), max(rlexp),'k',linewidth=0.5)
ax1.set_title('Bifuraction Diagram and Lyapunov Exponents: Logistic map')
ax1.set_ylabel('(x_n), lambda')
ax1.set_xlabel('Control parameter, r')
ax1.axis([0,2.0,-2.75,1.25])

rchaos = []
for i in range(N):
    if lexp[i] < 0:
        rchaos.append(rlexp[i])

# Get CDF for sum of iterates to check for central limit theorem
n_init = 100000 #number of initial values
n_iter3 = 1000 #number of iterations
n_iter5 = 10000 #number of iterations

# Sum of iterates for quadratic logistic equation 1

# Chaotic system, positive lyapunov exponents, Gaussian centered at 0
fig2, (ax2_1,ax2_2,ax2_3) = plt.subplots(3,1)

# subplot 1 | ax2_1 r=1.7 | n_init=10^5 | n_iter=10^3,10^5
ax2_1_iter1 = getSumOfIterates(1.7,n_init,n_iter3)
ax2_1_x1,ax2_1_y1 = getHistPoints(ax2_1_iter1)
ax2_1.plot(ax2_1_x1,ax2_1_y1,'b.',label='n_iter=10^3')
ax2_1_yfit1 = getFit(ax2_1_x1,ax2_1_y1)
ax2_1.plot(ax2_1_x1,ax2_1_yfit1,'b-',linewidth=0.5) #_____
ax2_1_iter2 = getSumOfIterates(1.7,n_init,n_iter5)
ax2_1_x2,ax2_1_y2 = getHistPoints(ax2_1_iter2)
ax2_1.plot(ax2_1_x2,ax2_1_y2,'m.',label='n_iter=10^5')
ax2_1_yfit2 = getFit(ax2_1_x2,ax2_1_y2)
ax2_1.plot(ax2_1_x2,ax2_1_yfit2,'m-',linewidth=0.5)

ax2_1.annotate('r=1.7',(100,100))
ax2_1.legend()

# subplot 2 | ax2_2 r=1.8 | n_init=10^5 | n_iter=10^3,10^5
ax2_2_iter1 = getSumOfIterates(1.8,n_init,n_iter3)
ax2_2_x1,ax2_2_y1 = getHistPoints(ax2_2_iter1)
ax2_2.plot(ax2_2_x1,ax2_2_y1,'b.',label='n_iter=10^3')
ax2_2_yfit1 = getFit(ax2_2_x1,ax2_2_y1)
ax2_2.plot(ax2_2_x1,ax2_2_yfit1,'b-',linewidth=0.5) #_____
ax2_2_iter2 = getSumOfIterates(1.8,n_init,n_iter5)
ax2_2_x2,ax2_2_y2 = getHistPoints(ax2_2_iter2)
ax2_2.plot(ax2_2_x2,ax2_2_y2,'m.',label='n_iter=10^5')
ax2_2_yfit2 = getFit(ax2_2_x2,ax2_1_y2)
ax2_2.plot(ax2_2_x2,ax2_2_yfit2,'m-',linewidth=0.5)
ax2_2.annotate('r=1.8',(100,100))
ax2_2.legend()

# subplot 3 | ax2_3 r=1.7,1.8,1.9,2.0 | n_init=10^5 | n_iter=10^3
ax2_3.plot(ax2_1_x1,ax2_1_y1,'r.',label='r=1.7')
ax2_3.plot(ax2_1_x1,ax2_1_yfit1,'r-',linewidth=0.5)
ax2_3.plot(ax2_2_x1,ax2_2_y1,'g.',label='r=1.8')
ax2_3.plot(ax2_2_x1,ax2_2_yfit1,'g-',linewidth=0.5) #_____
ax2_3_iter3 = getSumOfIterates(1.9,n_init,n_iter3)
ax2_3_x3,ax2_3_y3 = getHistPoints(ax2_3_iter3)
ax2_3.plot(ax2_3_x3,ax2_3_y3,'b.',label='r=1.9')
ax2_3_yfit3 = getFit(ax2_3_x3,ax2_3_y3)
ax2_3.plot(ax2_3_x3,ax2_3_yfit3,'b-',linewidth=0.5) #_____
ax2_3_iter4 = getSumOfIterates(2.0,n_init,n_iter3)
ax2_3_x4,ax2_3_y4 = getHistPoints(ax2_3_iter4)
ax2_3.plot(ax2_3_x4,ax2_3_y4,'m.',label='r=2.0')
ax2_3_yfit4 = getFit(ax2_3_x4,ax2_3_y4)
ax2_3.plot(ax2_3_x4,ax2_3_yfit4,'m-',linewidth=0.5)
ax2_3.legend()
ax2_2.set_ylabel('Frequency')
ax2_3.set_xlabel('Sum of Iterates')

# Cahotic and non-chaotic
fig3, (ax3_1,ax3_2) = plt.subplots(2,1)

# Chaotic system
# Positive lyapunov exponents, Gaussian centered at 0
#   r = 0.74545, 2.0 - period doubling, larger spread
ax3_1_iter1 = getSumOfIterates(0.74545,n_init,n_iter3)
ax3_1_x1,ax3_1_y1 = getHistPoints(ax3_1_iter1)
ax3_1.plot(ax3_1_x1,ax3_1_y1,'b.',label='r=0.74545')
ax3_1_yfit1 = getFit(ax3_1_x1,ax3_1_y1)
ax3_1.plot(ax3_1_x1,ax3_1_yfit1,'b-',linewidth=0.5)
ax3_1.plot(ax2_3_x4,ax2_3_y4,'m.',label='r=2.0')
ax3_1.plot(ax2_3_x4,ax2_3_yfit4,'m-',linewidth=0.5)
ax3_1.legend()

# Non-chaotic system
# Negative lyapunov exponents, Gaussian not centered at 0
#   r = 1.5751503006, 1.75531062124
ax3_2_iter1 = getSumOfIterates(1.5751503006,n_init,n_iter3)
ax3_2_x1,ax3_2_y1 = getHistPoints(ax3_2_iter1)
ax3_2.plot(ax3_2_x1,ax3_2_y1,'b.',label='r=1.5751503006')
ax3_2_yfit1 = getFit(ax3_2_x1,ax3_2_y1)
ax3_2.plot(ax3_2_x1,ax3_2_yfit1,'b-',linewidth=0.5) #_____
ax3_2_iter2 = getSumOfIterates(1.75531062124,n_init,n_iter3)
ax3_2_x2,ax3_2_y2 = getHistPoints(ax3_2_iter2)
ax3_2.plot(ax3_2_x2,ax3_2_y2,'m.',label='r=1.75531062124')
ax3_2_yfit2 = getFit(ax3_2_x2,ax3_2_y2)
ax3_2.plot(ax3_2_x2,ax3_2_yfit2,'m-',linewidth=0.5)
ax3_2.legend()
ax3_2.set_ylabel('Frequency')
ax3_2.set_xlabel('Sum of Iterates')

plt.show()