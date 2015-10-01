import math
def ifAbundant(n):
    sum=1
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i==0):
            if i==n/i:
                sum+=i
            else:
                sum+=i
                sum+=n/i
    if sum>n:
        return True
    return False
print(ifAbundant(12))
a=[]
for i in range(10,28123,1):
    if ifAbundant(i):
        a.append(i)

b=set()
for i in range(len(a)):
    for j in range(len(a)):
        if( a[i]+a[j]<28123):
            b.add(a[i]+a[j])
sum=0
for i in range(28123):
    if not(i in b):
        sum+=i
print(sum)
 
