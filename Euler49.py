def ifpermu(n):
    a=list()
    s=list()
    for i in range(len (n)):
        s.append(str(n[i]))
    for i in range(len(s[0])):
        a.append(s[0][i])
    for i in range(len (s)):
        temp=a.copy()
        for j in range(len (s[i])):
            if( s[i][j] not in temp):
                return False
            else:
                temp.remove(s[i][j])
    return True
def sieve(n):
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

p= sorted(list(set(sieve(11000))));

           

for i in range(169,600,1):
    for j in range (169,1250,1):
        k=p[j]*2-p[i]
        if(k in p and k!=i and k!=j and i!=j and k<10000 and k>1000):
            if(ifpermu([p[i],p[j],k])):
                print('Set')
                print(str(p[i]))
                print(str(p[j]))
                print(str(k))
