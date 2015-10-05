#a**2+b**2=c**2 a+b+c=P
#a**2+b**2=(p-a-b)**2
#p^2-2pa-2pb-2ab=0
#b=p(p-2a)/2(p-a)
tmax=0
index=0
for p in range(250,1000,2):
    times=0
    for a in range(2,int(p/3)+2,1):
        if p*(p-2*a)%(2*(p-a))==0:
            times+=1;
    if times>tmax:
        tmax=times
        index=p
print(index)
