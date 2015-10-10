def sort(tempList, first):
    newList=[]
    for i in range(first,10):
        newList.append(tempList[i])
    newList.sort()
    del tempList[first:10]
    for i in range(len(newList)):
        tempList.append(newList[i])

def swap(tempList,a,b):
    temp=tempList[a]
    tempList[a]=tempList[b]
    tempList[b]=temp
def findFirst(tempList):
    for i in range(8,-1,-1):
        if tempList[i]<tempList[i+1]:
            return i
def findSecound(tempList, first):
    secound=0
    minNum=10
    for i in range(first+1,10):
        num=tempList[i]
        if(num>tempList[first]and num<=minNum):
            minNum=num
            secound=i
    return secound
def getNext(tempList):
    first=findFirst(tempList)
    secound=findSecound(tempList,first)
    swap(tempList,first,secound)
    sort(tempList, first+1)
def stop(list1, list2):
    for i in range(len(list1)):
        if(list1[i]!= list2[i]):
            return False
    return True
def divi(li):
    if(li[3]%2==0 and(li[2]+li[3]+li[4])%3==0 and li[5]%5==0 and (li[4]*100+li[5]*10+li[6])%7==0 and (li[5]*100+li[6]*10+li[7])%11==0 and (li[6]*100+li[7]*10+li[8])%13==0 and (li[7]*100+li[8]*10+li[9])%17==0):
        return True
    return False
list2=[9,8,7,6,5,4,3,2,1,0]
list1=[0,1,2,3,4,5,6,7,8,9]


tsum=0
while( not stop(list1, list2)):
    if divi(list1):
        tsum+=int(''.join(map(str,list1)))
    getNext(list1)
print(tsum)

    
 
 
