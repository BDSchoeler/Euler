import math
def getPent(n):
    return n*(3*n-1)/2
def ifPent(n):
    temp=(math.sqrt(24*n+1)+1)/6
    if temp==int(temp):
        return True
    return False


i=1    
notFound=True
while notFound:
    high= getPent(i)
    for j in range(i-1,0,-1):
        low= getPent(j)
        if(ifPent(low+high) and ifPent(high-low)):
            print (high-low)
            break
    i=i+1
print ('end')
