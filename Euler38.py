def ifPandigital(nums):
    lsum=0
    s=[]
    for i in range (len(nums)):
        s.append(str(nums[i]))
        lsum+=len(s[i])
    if(lsum==9):
        a=[]
        for j in (range(len(s))):
            for i in (range(len(s[j]))):
                if s[j][i] in a or s[j][i]=='0':
                    return False
                else:
                    a.append(s[j][i])
        return True
    return False
def merge(nums):
    s=""
    for i in range (len(nums)):
        s+=(str(nums[i]))
    return int(s)

lmax=0
for i in range(1,100,1):
    a=[]
    for j in range(1,5,1):
        a.append(i*j)
    if ifPandigital(a):
        temp=merge(a)
        if lmax<temp:
            lmax=temp
            print(temp)
        

for i in range(100,333,1):
    a=[]
    for j in range(1,4,1):
        a.append(i*j)
    if ifPandigital(a):
        temp=merge(a)
        if lmax<temp:
            lmax=temp
            print(temp)
        

for i in range(333,10000,1):
    a=[]
    for j in range(1,3,1):
        a.append(i*j)
    if ifPandigital(a):
        temp=merge(a)
        if lmax<temp:
            lmax=temp
            print(temp)
