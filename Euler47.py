import math
def sieve(n):
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def numberPrimeFactors(n, primes):
    count=0
    current=n

    for i in range(len(primes)):
        
        ifdivided=False
        while(current%primes[i]==0):
            ifdivided=True
            current=current/primes[i]
        if(ifdivided):
            count+=1
        if current==1:
            return count
        if primes[i]*primes[i]>n:
            return count+1


primes = sorted(list(set(sieve(10000))));
num=200
count=0
while(count<4):
    num+=1
    if(numberPrimeFactors(num,primes)==4):
        count+=1
    else:
        count=0
print(num-3) 
    
