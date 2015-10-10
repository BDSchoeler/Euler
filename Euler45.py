
def p(n):
    return n*(3*n-1)/2
def h(n):
    return n*(2*n-1)



iP=200
iH=200

while(p(iP) != h(iH)):
    temp=p(iP)
    if(temp> h(iH)):
        iH+=1
    iP+=1
print(h(iH))
                  
