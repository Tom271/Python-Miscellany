#Factor Finder
#Finds all integer factors
import math
import csv

def isPrime(n):
    isPrimeRet=True
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i==0:
                isPrimeRet = False
                break
        return isPrimeRet
t=0
for t in range(0,6):
    x=raw_input('What number is to be tested?')
    x=float(x)
    if isPrime(x)==True:
        print "Prime"
    else:
        print"Not Prime"
    t+=1

