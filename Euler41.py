import math
def ifPandigital(num):
    s=str(num)
    a=[]
    for i in (range(len(s))):
        if s[i] in a or s[i]=='9' or s[i]=='8' or s[i]=='0':
             return False
        else:
            a.append(s[i])
    return True

def sieve(n):
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
smax=0
primes = set(sieve(10000000))
for i in range(1000001,10000000,2):
    if(i in primes and ifPandigital(i)):
        smax=i
print(smax)
