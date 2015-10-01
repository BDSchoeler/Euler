def ifPandigital(num1,num2,num3):
    s=[str(num1),str(num2),str(num3)]
    
    if(len(s[0])+len(s[1])+len(s[2])==9):
        a=[]
        for j in range(len(s)):
            for i in range(len(s[j])):
                if s[j][i] in a or s[j][i]=='0':
                    return False
                else:
                    a.append(s[j][i])
        return True
    return False

rsum=0
a=set()
for i in range(1000):
    
    for j in range(123,int(10000/(i+1)),1):
        prod=i*j
        if ifPandigital(i,j,prod):
            a.add(prod)
s=len(a)
for i in range(s):
    rsum+=a.pop()
print(rsum)
    
    
