import numpy as npy

a = 'fizz'
b = 'buzz'

for i in range(1,101):
    mod3 = i%3
    mod5 = i%5
    mod15 = i%15

    if (mod3 == mod5 == 0):
        print(a,b)
    elif (mod3 == 0):
            print(a)
    elif (mod5 == 0):
            print(b)
    else:
        print(i)
