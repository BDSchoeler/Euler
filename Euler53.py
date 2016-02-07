import math
def CC(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
num=0

for i in range(1,101,1):
    for j in range(1,i+1,1):
        if( CC(i,j)>1000000):
            num+=1
print(num)
print(CC(23,10))
