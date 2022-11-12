import scipy as s
import numpy as npy
import random as rand
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

global xf
xf = npy.zeros((201,201),int)

##middle is 100. add 100 to x,y coordinate to make 100,100 the origin
global lmax,center
lmax = len(xf)
center = int(lmax/2)

### create seed
xf[center,center] = 1

global rmax,rkill,rs,rx,ry
rmax = 0
rkill = 50
rd = 49
rs = 5
phi = rand.random()*(2*npy.pi)
rx = rs*npy.sin(phi)
ry = rs*npy.cos(phi)

img = Image.new("RGB",(201,201),(255,255,255))
draw = ImageDraw.Draw(img)

### generate random angle
def occupy():
    global rx,ry
    phi = rand.random()*(2*npy.pi)
    rx = rs*npy.sin(phi)
    ry = rs*npy.cos(phi)

### make it move
def jump():
    global rx,ry
    r = rand.randint(1,4)
    if r == 1:
        rx = rx+1
    elif r == 2:
        rx = rx-1
    elif r == 3:
        ry = ry+1
    elif r == 4:
        ry = ry-1

### check its adjacent points
def check():
    global rkill,rx,ry,rd,xf
    x = rx
    y = ry
    r = npy.sqrt(x*x+y*y)
    #is it in the kill region?

    xR = round(rx+1+center)
    xL = round(rx-1+center)
    xC = round(rx+center)
    yT = round(ry+1+center)
    yB = round(ry-1+center)
    yC = round(ry+center)

    if r > rkill:
        return 'k'
    elif r >= rd:
        return 'c'
    #does it have a neighbor? if yes, set it fixed
    elif xf[xR][yC] + xf[xL][yC] + xf[xC][yT] + xf[xC][yB] > 0:
        return 'a'
    #otherwise
    else:
        return 'j'

### make it stick to the aggregate
def aggregate():
    global rmax,rx,ry,rs,rd,rkill,xf
    xC = round(rx+center)
    yC = round(ry+center)
    xf[xC][yC] = 1
    x = rx
    y = ry
    if rmax <= npy.sqrt(x*x+y*y):
        rmax = npy.sqrt(x*x+y*y)
        rs = 5 + rmax
        rd = 49 + rmax
        rkill = 50 + rmax

    draw.point((xC,yC),(0,255,100))

### circlejump
def circlejump():
    global rx,ry,rs
    phi = rand.random()*2*npy.pi
    x = rx
    y = ry
    r = npy.sqrt(x*x+y*y)
    rx = rx+(r-rs)*npy.sin(phi)
    ry = ry+(r-rs)*npy.cos(phi)

### main part
particles = 1000
killed = 0
agg = 0
while particles != 0:
    part = check()
    if part == 'k':
        occupy()
        jump()
        particles = particles-1
        killed += 1
    elif part == 'a':
        aggregate()
        occupy()
        jump()
        particles = particles-1
        agg += 1
    elif part == 'j':
        jump()
    elif part == 'c':
        circlejump()
print("killed = ", killed)
print("aggregated = ", agg)
img.save("fractalaggregate.png","PNG")
