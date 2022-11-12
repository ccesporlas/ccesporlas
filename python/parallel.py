import parallel
import scipy, numpy as npy
import time
def sqr():
    s = []
    for i in range(100):
        s.append(0)
    for i in range(100):
        s.append(255)
##    sq = []
##    for i in range(10000):
##        for j in s:
##            sq.append(j)
    sq = npy.tile(s,1000)
    return sq

def tri():
    d = range(0,255)
##    d = list(scipy.linspace(0,255,10))
    for i in reversed(d):
        d.append(i)
##    tr = []
##    for i in range(10000):
##        for j in t:
##            tr.append(j)
    tr = npy.tile(d,10000)
    return tr

def sn():
    f = 128+npy.sin(npy.linspace(0,2*npy.pi,100))*127
    si = npy.tile(f,10)
    return si

p = parallel.Parallel()
tr = sqr()
#print tr

for i in tr:
    time.sleep(0.01)
    p.setData(int(i))
