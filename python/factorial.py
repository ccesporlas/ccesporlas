def factorial(n):
    if n<0:
        return None
    elif n%1>0:
        return None
    elif n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
