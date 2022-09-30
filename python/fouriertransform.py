#############################################################################################
# Name: Fourier Transform
# Description: This outputs the plot of a voltage signal using the set of Fourier
# coefficients b (with problem1: constant phases, problem2: random phases)
# where these coefficients are the Fourier transform of a set of voltage
# values obtained from a number of probes N. This only gives approximation
# since the the voltage values are taken from a discrete number of sources.
# This also outputs an approximate minimum of the voltage peaks and the set of
# phase angles that give these values.
#############################################################################################

import matplotlib.pyplot as plt
import numpy as n, numpy.random as nrand, numpy.fft as nfft

N = 100 #number of voltage probes, increase to make the signal more defined
x = n.linspace(0,N-1,N)

#problem 1
plt.figure(1)
b1 = n.zeros(N) #array of 64 zeroes

for i in range(8,17,2):
    #choose values we can change with some value
    b1[i] = 1
    b1[N-i] = 1

part1 = nfft.ifft(b1)
plt.plot(x,part1,'r-',label='Voltage Signal with Constant Phases',linewidth=0.7)
plt.axis('tight')
plt.xlabel('Voltage Signal Probes (N)')
plt.ylabel('Voltage Sequence(U)')

#problem 2
plt.figure(2)
b2 = n.zeros(N)

for i in range(8,17,2):
    #choose random values between 0 and 1, multiply by 360 to get randome phase in degrees
    bs = int(abs(n.exp(1j*nrand.rand()*360)))
    b2[i] = bs
    b2[N-i] = n.conjugate(bs)

part2 = nfft.ifft(b2)
plt.plot(x,part2,'b',label='Voltage Signal with Random Phases',linewidth=0.7)

plt.axis('tight')
plt.xlabel('Voltage Signal Probes (N)')
plt.ylabel('Voltage Sequence(U)')

#problem 3
plt.figure(3)
plt.axis('auto')
plt.xlabel('Voltage Signals (R3)')
plt.ylabel('Voltage Sequence(U)')

N3 = 100 #number of probes for one voltage signal
R3 = 100 #number of voltage signals
raxis = n.linspace(0,R3-1,R3)
x3 = n.linspace(0,N3-1,N3)

b3 = n.zeros(N3)

#create empty arrays to store maxU and phi values
#repeat what we did in part 2 multiple times to get multiple sets of signals and phases
phis = []
maxU = []

#get values of b and phi respectively
for r in range(R3):
    for nn in range(0,N3-1):
        for i in range(8,17,2):
            phi = nrand.rand()*360
            b3[i] = int(abs( n.exp(1j*phi) ))
            b3[N3-i] = n.conjugate(b3[i])

        #store generated and used phi values
        phis.append(phi)

    #get Fourier transform of set of b values
    U = n.real(nfft.ifft(b3))
    plt.plot(x3,U,'g',label='Voltage Signals with Different Sets of Random Phases',linewidth=0.7)

    #make a two dimensional array of the U value and the respective phi value used
    for j in range(N3-1):
        setU = [U[j],phis[j]]
        #print setU

    #Find the maximum U value for one voltage signal from N probes
    for j in range(N3):
        maximum = max(U)
        if U[j] == maximum:
            imax = [U[j],phis[j]]
            #print imax
    #print maximum

    #store obtained maximum U value in an array
    maxU.append(maximum)

#make a plot of the maximum U values
plt.figure(4)
plt.axis('auto')
plt.xlabel('Voltage Signal(R)')
plt.ylabel('Peak Voltage Values(maxU)')
plt.plot(raxis,maxU,'mo',label='Peak Voltages',markersize=0.9)

#Get the minimum of the set of maximum U values from R voltage signals
for r in range(R3):
    minmaxU = min(maxU)

#store the minimum of the set of maximum U values and the corresponding phi used in a two dimensional array
for j in range(N3):
    if U[j] == minmaxU:
        minU = [U[j],phis[j]]
        print(minU)

#show the minimum of the maximum U values
print(minmaxU)

plt.show()
