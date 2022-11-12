import random, numpy as npy
import scipy.special as sp
import matplotlib.pyplot as plt

def ipos(N):
    x = random.randint(0,N)
    y = random.randint(0,N)
    print (x,y)
    return (x,y)

def rand(num):
    ''' Both generators produce integers 0, 1, ..., 9 and repeat
    the sequence if the last five numbers have appeared before
    in the same order. Consequently, both have to repeat
    the sequence generated after at most $10^5$ steps. '''
    # (I) $r_n = (r_{n-2} - r_{n-5})$ mod 10
    # (II) $r_n = (r_{n-2} - r_{n-5} - c_{n-1})$ mod 10
    # given r_n = (r_{n-2} - r_{n-5} - c_{n-1})
    #  if       r_n <= 0,   c_n = 1
    #  else if  r_n > 0,    c_n = 0
    a = 106
    c = 1283
    m = 6075
    r0 = 1234
    x = []
    for i in range(num):
        rn = ( a*r0 + c ) % m
        x.append(rn)
        r0 = rn
    return x

# random matrix
N = 11
M = npy.zeros([N,N])

for i in range(N):
    for j in range(N):
        r = random.randint(0,N)
        M[i,j] = r

print(M[ipos(N-1)])
print(M)

# Random Number Generator 1
r0 = [100,39,1,7,3] # the initial set of values(seed)
N = 10000

# generate random numbers
for i in range(5,N):
    rn = (r0[i-2] - r0[i-5])%10
    r0.append(rn)

#get period
for a in range(5,N):
    if r0[a:a+5] == r0[0:5]:
        print(a)

ave = npy.mean(r0)  #get mean

#get histogram
plt.hist(r0, bins=10, normed=1)
plt.axis([-1,10,0,0.5])

# Random Number Generator 2
r0 = [100,39,1,7,3] #the initial set of values(seed)
c = 0   #initial value for c
N = 100000

#generate random numbers
for i in range(5,N):
    rn = (r0[i-2] - r0[i-5] - c)%10
    r0.append(rn)
    if (r0[i-2] - r0[i-5] - c)>0:
        c = 0
    else:
        c = 1

#get period
for a in range(10,N):
    if r0[a:a+5]==r0[5:10]:
        print(a-5)

ave = npy.mean(r0)  #get mean
#get histogram
plt.hist(r0, bins=10, normed=1)
plt.axis([-1,10,0,0.5])

#random walk
N = 20

n1 = npy.linspace(0, N, N+1)
m = (2*n1)-N
numerator = sp.factorial(N)
factor1 = sp.factorial((0.5)*(N+m))
factor2 = sp.factorial((0.5)*(N-m))
denominator = factor1*factor2
multiplier = (0.5)**N
P = (numerator/denominator)*multiplier
plt.plot(n1, P, 'o')

plt.show()