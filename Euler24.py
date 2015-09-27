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


list1=[0,1,2,3,4,5,6,7,8,9]

for i in range(999999):
    getNext(list1)
 
print(list1)
