def sieve(n):
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
def gold(n, primes):
    current=1
    j=1
    while( current<n+1):
        current=primes[j]
        value= current+2*1
        if value==n:
            return True
        k=2
        while value<=n:
            value=current+2*(k**2)
            if value==n:
                return True
            k+=1
        j+=1
    return False
                

primes = sorted(list(set(sieve(1000000))));


for i in range(23,1000000,2):
    if( i not in primes and not gold(i,primes)):
       print(i)
       break
print('done')
