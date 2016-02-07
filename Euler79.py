import math
f = open('p079_keylog.txt', 'r')
line= f.readline()
d1=[]
d2=[]
d3=[]
ex=[]
while (line!=""):
    numbers= line.replace("/n","").lstrip()
    d1.append(int(numbers[0]))
    d2.append(int(numbers[1]))
    d3.append(int(numbers[2]))
    line=f.readline()
print(d1)
left=[0,1,2,3,6,7,8,9]
pos=True
ans=[]
while(left!=[]):
    for j in left:
        i=0
        while( pos and i<len(d1)):
            if( d3[i]==j):
                if( d2[i] in left or d1[i] in left):
                    pos=False
            if( d2[i]==j):
                if(d1[i] in left):
                     pos=False
            i+=1
        if(pos):
            ans.append(j)
            left.remove(j)
        pos=True
print(ans)
    
