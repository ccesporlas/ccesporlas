import random, numpy as npy
import matplotlib.pyplot as plt

T = 10000
N = 100
D = 25
d = 1
xy = [npy.array([0,0])]
pi = npy.pi
minDistance = 4
killZone = 25.1

for n in range(1,N):
    stop=0
    xy.append(npy.zeros(2,float))
    angle = random.random()*2*pi
    xy[n][0] = int(D*npy.cos(angle))
    xy[n][1] = int(D*npy.sin(angle))
    for t in range(T):
        for n1 in  range(n-1):
            if ((xy[n][0]-xy[n1][0])*(xy[n][0]-xy[n1][0])+(xy[n][1]-xy[n1][1])*(xy[n][1]-xy[n1][1]) < minDistance):
                print(n,"HIT!")
                stop=1
                break

        if stop==1:
            break

        if (abs(xy[n][0]) > killZone) or (abs(xy[n][1]) > killZone):
            angle = random.random()*2*pi
            xy[n][0] = D*npy.cos(angle)
            xy[n][1] = D*npy.sin(angle)


        xory = random.randint(0,1)
        xy[n][xory] += random.randint(-1,1)*d
        if t == T-1:
            xy[n] = [0,0]
            print(n,"FAILED!")

xy = npy.array(xy)
plt.plot(xy[:,0],xy[:,1],'ro')
plt.show()
