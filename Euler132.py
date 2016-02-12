# r(n)= (10^n-1)/9
#(10^n-1)/9=0 mod p if p is a factor
#10^n=1 mod 9p
#
#
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
def expmod(a,b,c):
    if(b==1):
        return a%c
    x=expmod(a,b>>1,c)
    x=(x*x)%c
    if(b&1==1)==1:
        x=(x*a)%c
    return x
a=sieve(200000)
print("done")
count=0
num=(10**9)
i=3
s=0
while(count<40):
    temp=next(a)
    if( expmod(10,num,(temp*9))==1):
        s+=temp
        count+=1
    i+=1
    
print(s)
