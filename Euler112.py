import math
def getDigit(n,l):
    n=n//(math.pow(10,l-1))
    return int(n%10)
def ifIncreasing(n):
    l=len(str(n))
    old=getDigit(n,l)
    for i in range(l-1,0,-1):
        new=getDigit(n,i)
        if(old>new):
            return False
        old=new
    return True
def ifDecreasing(n):
    l=len(str(n))
    old=getDigit(n,l)
    for i in range(l-1,0,-1):
        new=getDigit(n,i)
        if(old<new):
            return False
        old=new
    return True
def ifBouncy(n):
    return not ifDecreasing(n) and not ifIncreasing(n)
    
ratio=0.9
number=21780
numberB=0.9*21780
while numberB*100<number*99:
    if ifBouncy(number):
        numberB+=1
    number+=1
print(number)



