import math
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
def sieve(n):
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
primes = sorted(list(set(sieve(1000010))));
print("done")
primeSum= [0];
f=1
hmax=0
highestprime=0;
while(primes[f]<10000):
    primeSum.append(primeSum[f-1]+ primes[f-1])
    f+=1
for i in range(len(primeSum)):
    for j in range(i):
        if(binarySearch(primes, primeSum[i]-primeSum[j])):
            if(hmax<i-j):
                hmax=i-j
                highestprime= primeSum[i]-primeSum[j]
           
print(highestprime)
