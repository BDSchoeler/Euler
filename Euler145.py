def ifRev(n):
    if n%10==0:
        return False
    num=n+int(str(n)[::-1])
    return ifOdd(num)
def ifOdd(n):
    num=int(n)
    for i in range(len(str(n))):
        if(num%10)%2==0:
            return False
        num=num//10
    return True


count=0
for i in range(10,100000000,1):
    if(ifRev(i)):
       count+=1
print(count)
