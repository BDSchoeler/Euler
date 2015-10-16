def containsOrigin(a,b,c):
    AB=[a[0]-b[0],a[1]-b[1]]
    BC=[b[0]-c[0],b[1]-c[1]]
    CA=[c[0]-a[0],c[1]-a[1]]
    if (cp(AB,a)>0 and cp(BC,b)>0 and cp(CA,c)>0) or (cp(AB,a)<0 and cp(BC,b)<0 and cp(CA,c)<0):
        return True
    return False
def cp(a,b):
    return a[0]*b[1]-a[1]*b[0]
     
    


f = open('triangles.txt','r')
lines=f.readlines()
count=0
for i in lines:
    i=i.split(',');
    i=[[int(i[0]),int(i[1])],[int(i[2]),int(i[3])],[int(i[4]),int(i[5].rstrip('\n'))]]
    if containsOrigin(i[0],i[1],i[2]):
       count+=1
       print(i)
print(count)

