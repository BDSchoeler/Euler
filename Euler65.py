def sumDigits(n):
    ts=0
    for i in str(n):
        ts+=int(i)
    return ts

print(sumDigits(12345))
num=2
den=1
for i in range (2,101,1):
    n=0
    temp=den
    if(i%3==0):
        n=int((i/3)*2)
    else:
        n=1
    den=num
    num=n*num+temp

print(sumDigits(num))
