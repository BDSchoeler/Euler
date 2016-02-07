import math
f = open('p099_base_exp.txt', 'r')
line= f.readline()
mbase=1
mexp=1
base= []
exp=[]
i=0
m=0
while (line!="" and i <1000):
    numbers= line.replace("/n","").lstrip().split(",")
    base.append(int(numbers[0]))
    exp.append(int(numbers[1]))
    if( math.log(mbase)*mexp< math.log(base[i])*exp[i]):
        mbase=base[i]
        mexp=exp[i]
        m=i
    i+=1
    line=f.readline()
print(mbase)
print(mexp)
print(m)
