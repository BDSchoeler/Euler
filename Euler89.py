
import math

def toDec(st):
    ts=0
    c=0
    d= {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000 
    }
    notdone=True
    while(notdone):
        if(st[c]=='M'):
            ts+=1000
        if(st[c]=='D'):
            ts+=500
        if(st[c]=='C'):
            if(st[c+1]=='D'):
                ts+=400
                c+=1
            elif(st[c+1]=='M'):
                ts+=900
                c+=1
            else:
                ts+=100
        if(st[c]=='L'):
            ts+=50
        if(st[c]=='X'):
            if(st[c+1]=='L'):
                ts+=40
                c+=1
            elif(st[c+1]=='C'):
                ts+=90
                c+=1
            else:
                ts+=10
        if(st[c]=='V'):
            ts+=5
        if(st[c]=='I'):
            if(st[c+1]=='V'):
                ts+=4
                c+=1
            elif(st[c+1]=='X'):
                ts+=9
                c+=1
            else:
                ts+=1
        c+=1
        if(c==len(st)-1):
            ts+=d[st[c]]
            notdone=False
        if(c==len(st)):
            notdone=False
    return ts
def ld(num):
    c=0
    while(num/1000>=1):
        num-=1000
        c+=1;
    while(num/900>=1):
        num-=900
        c+=2;
    while(num/500>=1):
        num-=500
        c+=1;
    while(num/400>=1):
        num-=400
        c+=2;
    while(num/100>=1):
        num-=100
        c+=1;
    while(num/90>=1):
        num-=90
        c+=2;
    while(num/50>=1):
        num-=50
        c+=1;
    while(num/40>=1):
        num-=40
        c+=2;
    while(num/10>=1):
        num-=10
        c+=1;
    while(num/9>=1):
        num-=9
        c+=2;
    while(num/5>=1):
        num-=5
        c+=1;
    while(num/4>=1):
        num-=4
        c+=2;
    while(num/1>=1):
        num-=1
        c+=1;
    return c
       
              
f = open('p089_roman.txt', 'r')

line=f.readline()
reduction=0
while(line !=""):
    reduction+= len(line.strip())-ld(toDec(line.strip()))
    line=f.readline()
print(reduction)
    
