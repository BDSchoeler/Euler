
def ifcurios(n,m):
    n1=n//10
    n2=n%10
    m1=m//10
    m2=m%10
    if (n2==m1 and n/m == n1/m2): #or (m2== n1 and n/m == n2/m1):
        return True
    return False




numerater=1
denominater=1
for i in range(10,100,1):
    for j in range(10,100,1):
        if i%10!=0 and j%10!=0:
            if ifcurios(i,j):
                numerater*=i
                denominater*=j



print(numerater)
print(denominater)
