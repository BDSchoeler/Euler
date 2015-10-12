def wordValue(n):
    lsum=0
    for i in range(len(n)):
        lsum+= ord(n[i])-ord('A')+1
    return lsum



f = open('words.txt','r')
t=(f.read().split('","'))
count=1
abc=[1]
for d in range(75):
    abc.append(d*(d+1)/2)

for b in range(1,len(t)-1,1):
    if(wordValue(t[b])in abc):
        count+=1
print(count)
