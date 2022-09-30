import numpy, matplotlib.pyplot as plt

def f(r,x):
    return 4*r*x*(1.0-x)

def df(r,x):
    return 4*r-8*r*x

N = 2000
rrange = numpy.linspace(0.1,1,2000)

#Create arrays to store lyapunov exponents at each parameter value
lexp = []
rlexp = []

for r in rrange:
    #Set initial condition
    x_n = 0.65

    #Remove initial transient iterations
    for i in range(100):
        x_n = f(r,x_n)

    #Bifurcation
    rlist = []
    x = []

    for i in range(N):
        x_n = f(r,x_n)
        rlist.append(r)
        x.append(x_n)
    plt.plot(rlist, x, 'r,')

    #Estimate lyapunov exponents over N iterations
    l = 0.0

    for i in range(N):
        x_n = f(r,x_n)
        l = l + numpy.log(abs(df(r,x_n)))

    #Get average of lyapunov exponent per iteration
    l = l/float(N)
    lexp.append(l)
    rlexp.append(r)
    plt.plot(rlexp,lexp,'g-',linewidth=0.6)

plt.axis([0.1,1.0,-7.5,1])
#plt.axis([0.7,1.0,-3.5,1])
#plt.axis([0.85,1.0,-1.5,1])
plt.title('Bifuraction Diagram and Lyapunov Exponents: Logistic map f(x)=4rx(1-x)')
plt.xlabel('Control parameter, r ')
plt.ylabel('(x_n), lambda')
plt.show()