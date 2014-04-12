#Prime Generator using the SIeve of Eratosthenes
#Upper limit 'n':
n=int(raw_input('Range?'))
numbers=range(1,n)
notprime=[]
p=range(2,n)
q=int(p[0])
while :
    for i in range(1,n):
        notprime.append(i*q)
        prime = [x for x in numbers if x not in notprime]
        p = [x for x in numbers if x not in notprime]


print numbers
print notprime
print prime
    
