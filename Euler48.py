import math
totalsum=0
tempSum=1
limit=int(math.pow(10,10))
for i in range(1001):
    tempSum=1
    for j in range(i):
        tempSum=tempSum*i
        tempSum=tempSum%limit
    totalsum= (totalsum+tempSum)%limit
print (totalsum-1)
        
    
