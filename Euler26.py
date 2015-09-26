def repititionLenght(n):
    newRemainder=10
    remainder= set()
    ifDone=True
    while  ifDone:
        newRemainder=newRemainder%n
        newRemainder=newRemainder*10
        ifDone=newRemainder not in remainder
        remainder.add(newRemainder)
    return len(remainder)

lmax=0
index=0
i=10
while i<1000:
    length=repititionLenght(i)
    if lmax<length:
        lmax=length
        index=i
    i=i+1
print(lmax)
print(index)
