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

def ifPrime(n):
    if(n%2==0):
        return False
    
    for i in range (3,int(math.sqrt(n)+1),2):
        if n%i==0:
            return False
    return True
def dropLow(n):
    return n//10

def dropHigh(n):
    length=len(str(n))
    
    return n% int(math.pow(10,length-1))
    
a=[2]
count=0
tsum=0
for i in range(3,1000000,2):
    if ifPrime(i):
        a.append(i)
for i in range(4,len(a),1):
    num1=a[i]
    num2=a[i]
    check=True
 
    for j in range(len(str(a[i]))-1): 
        num1=dropLow(num1)
        num2=dropHigh(num2)
        if not(binarySearch(a,num1) and binarySearch(a,num2)):
            check=False
            break
    if(check):
        tsum+=a[i]
print(tsum)
               


