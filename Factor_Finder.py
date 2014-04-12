#Factor Finder
#Finds all integer factors
import math
import csv


x=raw_input('What number is to be tested?')
x=float(x)
num=[]
time=[]
xrang=math.sqrt(x)+ 1
rang=int(xrang)
for i in range (1,rang):
    if x % i==0:
        print i,"is a factor!"
        num.append(i)
    
        
if len(num)==1:
    print "Prime!"
if int(xrang)==xrang:
    print "Perfect Square!"

print num        
