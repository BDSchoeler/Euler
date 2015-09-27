import math
def firstDigit(n):
    l=len(str(n))
    return n//(math.pow(10,l-1))
def deleteFirstDigit(n):
    l=len(str(n))
    return n%(math.pow(10,l-1))
def champerDigit(n):
     count=0
     num=1
     while(count<n):
         l=len(str(num))
         i=0
         tempnum=num
         while(i<l and count<n):
            currentnum= firstDigit(tempnum)
            tempnum= int(deleteFirstDigit(tempnum))
            count= count+1
            i+=1
         num+=1
     return currentnum    
         
product=1
count=10
for i in range(6):
    product*=champerDigit(count)
    count*=10
print(product)
